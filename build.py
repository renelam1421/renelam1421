top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

index = open('content/index.html').read()
about = open('content/about.html').read()
contact = open('content/contact.html').read()
posts = open('content/posts.html').read()
projects = open('content/projects.html').read()

combine_index = top + index + bottom
combine_about = top + about + bottom
combine_contact = top + contact + bottom
combine_posts = top + posts + bottom
combine_projects = top + projects + bottom

open('docs/index.html', 'w').write(combine_index)
open('docs/about.html', 'w').write(combine_about)
open('docs/contact.html', 'w').write(combine_contact)
open('docs/posts.html', 'w').write(combine_posts)
open('docs/projects.html', 'w').write(combine_projects)
