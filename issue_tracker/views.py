import math
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from authentication.models import UserProfile
from issue_tracker.models import Issue, Comment
from django.contrib.auth.models import User
from issue_tracker.forms import IssueForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def get_all_issues(request):
    """
    Create a view that will return all the Issues from all Users
    that were published prior to now and render them all to issues.html
    template
    """ 
    all_issues = Issue.objects.filter(published_date__lte=timezone.now()).order_by("-total_votes")
    paginator = Paginator(all_issues, 2)
    page = request.GET.get('page')
    try:
        all_issues = paginator.page(page)
    except PageNotAnInteger:
        all_issues = paginator.page(1)
    except EmptyPage:
        all_issues = paginator.page(paginator.num_pages)
    paginator.page(paginator.num_pages)  
    return render(request, "issues.html", {"all_issues": all_issues})

def single_issue(request, pk):
    """
    Create a view that returns an issue based on the issue id (pk)
    and render it to viewissue.html or return 404 error if issue is not found
    """
    issue = get_object_or_404(Issue, pk=pk)
    comments = Comment.objects.filter(issue=issue).order_by("-id")
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(issue=issue,
                                             user_logged_in=request.user,
                                             content=content)
            comment.save()
            return redirect(single_issue, issue.pk)
        
    else:
        comment_form = CommentForm()
    
    author_image = []
    try:
        image = UserProfile.objects.get(user=issue.author).image
        author_image.append({"image": image})
    except:
        author_image.append({"image": None})
    
    # import pdb;pdb.set_trace()
        
    comments_with_images = []
    for comment in comments:
        try:
            image = UserProfile.objects.get(user=comment.user_logged_in).image
            comments_with_images.append({"image": image, "comment": comment})
        except:
            comments_with_images.append({"image": None, "comment": comment})
    comment_count = comments.count()
    # print(comment_count)
    # import pdb;pdb.set_trace()
    return render(request, "viewissue.html", {"author_image": author_image,
                                              "issue": issue,
                                              "comments_with_images": comments_with_images,
                                              "comment_count": comment_count,
                                              "comment_form": comment_form,
                                              })

def create_or_edit_issue(request, pk=None):
    """
    Create a view that allows the user to create or edit
    an issue depending if the issue ID is null or not
    """
    issue = get_object_or_404(Issue, pk=pk) if pk else None
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES, instance=issue)
        if form.is_valid():
            issue = form.save()
            issue.author = request.user
            issue.save()
            return redirect(single_issue, issue.pk)
    else:
        form = IssueForm(instance=issue)
    return render(request, "issueform.html", {"form": form})

def delete_issue(request, pk):
    """
    author of issue can delete their posted issue
    """
    issue = get_object_or_404(Issue, pk=pk)
    issue.delete()
    
    return redirect(get_all_issues)
    
def vote(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    user = request.user
    up_vote = True
    if user.is_authenticated():
        if user in issue.vote.all():
            issue.vote.remove(user)
            up_vote = False
        else:
            issue.vote.add(user)
    issue.total_votes = issue.vote.count()
    issue.save()
    print(up_vote)
    data = {
        "up_vote": up_vote
    }
    return JsonResponse(data)

@csrf_exempt
def done(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    data = {
        "is_done": issue.done
    }
    is_done = request.POST.get('is_done')
    if request.method == "POST":
        if str(is_done) == "true":
            issue.done = True;
            issue.save()
        else:
            issue.done = False;
            issue.save()
    return JsonResponse(data)

    
    