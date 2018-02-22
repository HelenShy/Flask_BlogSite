import my_blog.app as app

if __name__ == '__main__':
    #app = FlaskBlogSite.create_app()
    app = app.create_app()
    app.run()
