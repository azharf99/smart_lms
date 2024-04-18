"""
URL configuration for smart_lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from answers.views import AnswerViewSet, AnswerListView, AnswerCreateView, AnswerDetailView, AnswerUpdateView, AnswerDeleteView
from categories.views import CategoryViewSet, CategoryListView, CategoryCreateView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView
from contents.views import ContentViewSet, ContentListView, ContentCreateView, ContentDetailView, ContentUpdateView, ContentDeleteView
from courses.views import CourseViewSet, UserViewSet, CourseListView, CourseCreateView, CourseDetailView, CourseUpdateView, CourseDeleteView,\
                        UserListView, UserCreateView, UserDetailView, UserUpdateView, UserDeleteView
from enrollments.views import EnrollmentViewSet, EnrollmentListView, EnrollmentCreateView, EnrollmentDetailView, EnrollmentUpdateView, EnrollmentDeleteView
from grades.views import GradeViewSet, GradeListView, GradeCreateView, GradeDetailView, GradeUpdateView, GradeDeleteView
from lessons.views import LessonViewSet, LessonListView, LessonCreateView, LessonDetailView, LessonUpdateView, LessonDeleteView
from modules.views import ModuleViewSet, ModuleListView, ModuleCreateView, ModuleDetailView, ModuleUpdateView, ModuleDeleteView
from questions.views import QuestionViewSet, QuestionListView, QuestionCreateView, QuestionDetailView, QuestionUpdateView, QuestionDeleteView
from quizzes.views import QuizViewSet, QuizListView, QuizCreateView, QuizDetailView, QuizUpdateView, QuizDeleteView
from submissions.views import SubmissionViewSet, SubmissionListView, SubmissionCreateView, SubmissionDetailView, SubmissionUpdateView, SubmissionDeleteView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'submissions', SubmissionViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    # ... other urls
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('answers/', AnswerListView.as_view(), name='answer_list'),
    path('answers/<int:pk>/', AnswerDetailView.as_view(), name='answer_detail'),
    path('answers/create/', AnswerCreateView.as_view(), name='answer_create'),
    path('answers/<int:pk>/update/', AnswerUpdateView.as_view(), name='answer_update'),
    path('answers/<int:pk>/delete/', AnswerDeleteView.as_view(), name='answer_delete'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('contents/', ContentListView.as_view(), name='content_list'),
    path('contents/<int:pk>/', ContentDetailView.as_view(), name='content_detail'),
    path('contents/create/', ContentCreateView.as_view(), name='content_create'),
    path('contents/<int:pk>/update/', ContentUpdateView.as_view(), name='content_update'),
    path('contents/<int:pk>/delete/', ContentDeleteView.as_view(), name='content_delete'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('courses/create/', CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    path('enrollments/', EnrollmentListView.as_view(), name='enrollment_list'),
    path('enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment_detail'),
    path('enrollments/create/', EnrollmentCreateView.as_view(), name='enrollment_create'),
    path('enrollments/<int:pk>/update/', EnrollmentUpdateView.as_view(), name='enrollment_update'),
    path('enrollments/<int:pk>/delete/', EnrollmentDeleteView.as_view(), name='enrollment_delete'),
    path('grades/', GradeListView.as_view(), name='grade_list'),
    path('grades/<int:pk>/', GradeDetailView.as_view(), name='grade_detail'),
    path('grades/create/', GradeCreateView.as_view(), name='grade_create'),
    path('grades/<int:pk>/update/', GradeUpdateView.as_view(), name='grade_update'),
    path('grades/<int:pk>/delete/', GradeDeleteView.as_view(), name='grade_delete'),
    path('lessons/', LessonListView.as_view(), name='lesson_list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('lessons/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lessons/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lessons/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),
    path('modules/', ModuleListView.as_view(), name='module_list'),
    path('modules/<int:pk>/', ModuleDetailView.as_view(), name='module_detail'),
    path('modules/create/', ModuleCreateView.as_view(), name='module_create'),
    path('modules/<int:pk>/update/', ModuleUpdateView.as_view(), name='module_update'),
    path('modules/<int:pk>/delete/', ModuleDeleteView.as_view(), name='module_delete'),
    path('questions/', QuestionListView.as_view(), name='question_list'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('questions/create/', QuestionCreateView.as_view(), name='question_create'),
    path('questions/<int:pk>/update/', QuestionUpdateView.as_view(), name='question_update'),
    path('questions/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question_delete'),
    path('quizzes/', QuizListView.as_view(), name='quiz_list'),
    path('quizzes/<int:pk>/', QuizDetailView.as_view(), name='quiz_detail'),
    path('quizzes/create/', QuizCreateView.as_view(), name='quiz_create'),
    path('quizzes/<int:pk>/update/', QuizUpdateView.as_view(), name='quiz_update'),
    path('quizzes/<int:pk>/delete/', QuizDeleteView.as_view(), name='quiz_delete'),
    path('submissions/', SubmissionListView.as_view(), name='submission_list'),
    path('submissions/<int:pk>/', SubmissionDetailView.as_view(), name='submission_detail'),
    path('submissions/create/', SubmissionCreateView.as_view(), name='submission_create'),
    path('submissions/<int:pk>/update/', SubmissionUpdateView.as_view(), name='submission_update'),
    path('submissions/<int:pk>/delete/', SubmissionDeleteView.as_view(), name='submission_delete'),
]
