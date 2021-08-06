Our website stuff lives here :)

It runs on [Zola](getzola.org/), which is a static site generator made with Rust!

* `content` is where most of the stuff is: all of the text and articles you see on the website is there.
    * `articles` is a folder with generic manuals and articles which has its own nice page.
    * `info` is just a service folder with an `about` page. probably will have to add more later
    * `readme` is a folder with the readme that shows up on the home page. it's a folder so that if we need to add any images later it will be easier.

* `static` is just for images, favicons and stuff.

* `templates` contains Tera HTML templates, with every page being pretty self-descriptive, but still:
    * `base.html` is the main html which is included in every page of the website, with almost all of the CSS and
    header/footer stuff.
    * `index.html` is the html for the main home page
    * `blog.html` is for the list of articles in a certain section
    * `article.html` is for a single Markdown article
    * `404.html` is just an error page.
    * we don't have one, but we should create an `anchor-link.html` and customize in-page anchor links style


**If you want to add a new article or update it, look into `contents`. New articles should be created in appropriate
directories with the right top TOML section!!!**
