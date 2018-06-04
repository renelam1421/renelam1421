pages = [
    {
        'filename': 'content/index.html',
        'title': 'Index',
    },
    {
        'filename': 'content/about.html',
        'title': 'About',
    },
    {
        'filename': 'content/contact.html',
        'title': 'Contact',
    },
    {
        'filename': 'content/posts.html',
        'title': 'Posts',
    },
    {
        'filename': 'content/projects.html',
        'title': 'Projects',
    },
]

def main():
    template = open('templates/base.html').read()

    for item in pages:
        content = open(item['filename']).read()
        finished_content = template.replace('{{content}}', content)
        page_name = str('docs/' + item['title'] + '.html')
        open(page_name, 'w+').write(finished_content)

if __name__ == '__main__':
  main()



# top = open('templates/top.html').read()
# bottom = open('templates/bottom.html').read()
#
# index = open('content/index.html').read()
# about = open('content/about.html').read()
# contact = open('content/contact.html').read()
# posts = open('content/posts.html').read()
# projects = open('content/projects.html').read()
#
# combine_index = top + index + bottom
# combine_about = top + about + bottom
# combine_contact = top + contact + bottom
# combine_posts = top + posts + bottom
# combine_projects = top + projects + bottom
#
# open('docs/index.html', 'w').write(combine_index)
# open('docs/about.html', 'w').write(combine_about)
# open('docs/contact.html', 'w').write(combine_contact)
# open('docs/posts.html', 'w').write(combine_posts)
# open('docs/projects.html', 'w').write(combine_projects)
