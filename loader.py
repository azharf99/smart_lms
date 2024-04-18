# import os

# directory = [
#     'answers', 'categories', 'contents', 'courses', 'enrollments', 'grades', 'lessons', 'modules', 'questions', 'quizzes', 'submissions'
# ]
# single_directory = [
#     'answer', 'category', 'content', 'course', 'enrollment', 'grade', 'lesson', 'module', 'question', 'quiz', 'submission'
# ]
# file_suffix = [
#     'detail.html',
#     'form.html',
#     'list.html',
#     'confirm_delete.html',
# ]

# for i in range(len(directory)):
#     # os.makedirs(f'{directory[i]}/templates/{directory[i]}/')
#     for suff in file_suffix:
#         file_path = os.path.join(f'{directory[i]}/templates/{directory[i]}/', f'{single_directory[i]}_{suff}')
#         with open(file_path, "w") as file:
#             data = ["{% extends 'base.html' %}\n",
#                     "{% block 'title' %}", "{{title}}", "{% endblock 'title' %}\n",
#                     "{% block 'form_title' %}", "{{form_title}}", "{% endblock 'form_title' %}\n",
#                     "{% block 'breadcrumbs' %}", "{{title}}", "{% endblock 'breadcrumbs' %}\n",
#                     "{% block 'content' %}", "{% endblock 'content' %}"]
#             file.writelines(data)
#         print(file_path)

#     # print(os.listdir(f'{name}/templates/{name}'))