# The Fast Supper

[The Fast Supper](https://github.com/richardreiter/the-fast-supper) is a blog website dedicated to provide more information regarding fasting and its health benefits.

The website is targeted at people who are curious about fasting, so these like-minded people can learn more about it, and engage, commenting on the blog posts.

![Responsive The Fast Supper](media/images/tfs-responsiveness.png)

Visit the live site [here.](https://the-fast-supper.herokuapp.com/)

## UX (User Experience)

### Project Goals

- Create a community in which fasting enthusiasts are able to learn more about the subject and exchange ideas through the comment board on the blog posts.
- Provide an educational platform, support and help motivate the users who are currently fasting or thinking about it.

### Target Audience

- Anyone who wants to learn more about fasting.
- People currently on a fast who need a bit of support.
- Fasting practicioners who want to exchange ideas with like-minded people.

### User Stories

Agile methodology tool:

  - GitHub Projects was used to create and [manage a Kanban board](https://github.com/richardreiter/the-fast-supper/projects/1), for planning and implementing this project's functionalities.
![Kanban Board The Fast Supper](media/images/tfs-kanban-board.png)

- As a Site User I can view a list of posts so that I can easily select one to view.
- As a Site User I can view a list of posts so that I can select one to read.
- As a Site User I can click on a post so that I can read the full content.
- As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral.
- As a Site User / Admin I can view comments on an individual post so that I can read the conversation.
- As a Site User I can register an account so that I can comment and like.
- As a Site User I can leave comments on a post so that I can be involved in the conversation.
- As a Site User I can like or unlike a post so that I can interact with the content.
- As a Site Admin I can create, read, update and delete posts (CRUD) so that I can manage my blog content both from the front and back-end.
- As a Site Admin I can create draft posts so that I can finish writing the content later.
- As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.


### Wireframes

The mockups below were done with the help of Balsamiq (for both desktop and mobile screens), these were useful to help visualise the project.

- Desktop:
  - Home page 
  ![Home Desktop Mockup](media/images/desk-wireframe-home.png)
  - Blog post page 
  ![Post Desktop Mockup](media/images/desk-wireframe-post.png)
  - Register page
  ![Register Desktop Mockup](media/images/desk-wireframe-register.png)
  - Login page
  ![Login Desktop Mockup](media/images/desk-wireframe-login.png)

- Mobile:
  - Home page 
  ![Home Mobile Mockup](media/images/mobile-wireframe-home.png)
  - Register page
  ![Register Mobile Mockup](media/images/mobile-wireframe-register.png)
  - Login page
  ![Login Mobile Mockup](media/images/mobile-wireframe-login.png)


### Design

- The colour scheme was generated with [Coolors.](https://coolors.co/5dfdcb-7cc6fe-f4faff-8789c0-08090a)
![Color scheme](media/images/palette.png)

- [Google Fonts](https://fonts.google.com/) was used for the website's fonts. Inspiration on the choice of fonts (Chivo & Playfair Display) came from [this blog post.](https://artisanthemes.io/best-google-fonts-combinations-modern-agency-website/)

![Fonts Used](media/images/fonts.png)

## Features

### Existing Features

- __Navigation Bar__

  - Navigation is a fully responsive feature on all pages, it includes links on the site's Logo (displaying to the left within the bar), Home, Register and Login pages (the 'Add Post' page only shows up for superusers).
    ![Navigation Bar Superuser Logged In](media/images/tfs-nav-logged-in-admin.png)
  - The Logout page shows up (and both Register/Login pages disappear) once the user has successfully registered/logged in.
    ![Navigation Bar Logged Out](media/images/tfs-nav-logged-out.png)
    ![Navigation Bar User Logged In](media/images/tfs-nav-logged-in-user.png)
  - The navigation looks the same in each page to allow for easy navigation (without the user having to use the ‘back’ button), taking the user through a logical journey.
  - This section makes it easy for the user to learn more about the site's different sections and contents.

- __About section__

  - About section at home page to welcome and let the users know what the site is about.
   ![About section](media/images/tfs-about-section.png)

- __Blog Posts section__

  - The Blog posts section displays six posts at a time (with featured images, author, titles, post date, excerpt), feturing pagination ("NEXT", "PREV" buttons show up), in case there are seven or more posts.
   ![Blog section](media/images/tfs-blog-post-section.png)

- __Footer__

  - The footer area consists of three social links of the blog (Facebook, Instagram and Twitter - all of them, if clicked, open on a separate tab) and a "Copyright 2022" writing.
  - Like the navigation section, the footer looks the same on each page (and features on all of the pages) to allow for easy navigation, taking the user through a logical journey.

![Footer](media/images/tfs-footer.png)

- __Blog Post page__

  - Featuring the post image, post title, post author and post date (two links "Edit" & "Delete" which only show up in case the logged in user is an admin).
    ![Post header](media/images/tfs-post-header.png)
  - Post body content, like and comment count.
    ![Post body](media/images/tfs-post-body.png)
  - Comment and likes counter which displays how many users liked that particular post, if the user clicks on the heart icon they like or unlike the post.
    ![Comments Likes counter](media/images/tfs-post-like-counter.png)
  - The comments section, features information displayed from all users who have posted comments, such as their username, date of the comment and comment's content. It also features a text field to the right, so users who are logged in are able to engage with each other/the post and submit a comment.
    ![Comment section](media/images/tfs-post-comment-section.png)
  - Comments moderation for the admins so they can approve or disapprove users' comments (once an user submits a comment, the message below appears to them).
    ![Comment message](media/images/tfs-post-comment-approval.png)

- __Add Post page__

  - If the user is logged in as an admin, they are able to add a blog post (both from the front and backend), simply by clicking on the "Add Post" navigation link.
  - The page features a form where the user can fill out all the details for the new post, such as title, slug, author, image (upload a featured image), content, status (draft or published).
    ![Add Post](media/images/tfs-add-post-page.png)

- __Edit Blog Post page__

  - If the user is logged in as an admin, they are able to Edit any of the Blog posts (both from the front and backend), simply by clicking on the "Edit" link at the blog post's header.
  - The page features a form where the user can edit the current post's details such as title, content and excerpt.
    ![Edit Post](media/images/tfs-edit-post-page.png)

- __Delete Blog Post page__

  - If the user is logged in as an admin, they are able to delete any of the Blog posts (both from the front and backend), simply by clicking on the "Delete" link at the blog post's header.
  - The page displays the selected post for deletion's title, a warning message and two buttons (delete, back home).
    ![Delete Post](media/images/tfs-delete-post-page.png)


### Features Left to Implement

- __Forum/Members Area__

  - Implementing a forum/members area in the future could be really beneficial for The Fast Supper community, so the users would be able to have accountability partners as opposed to just exchanging ideas via the blog posts.

## Technologies Used

### Languages Used

- [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python3](https://developer.mozilla.org/en-US/docs/Glossary/Python)

### Frameworks, Libraries & Programs Used

- [Balsamiq](https://balsamiq.com/)
  - Balsamiq was used to make desktop/mobile mockups in order to visualise the project.
- [Bootstrap](https://getbootstrap.com/)
  - Bootstrap template.
- [Cloudinary](https://cloudinary.com/)
  - Cloudinary was used to store the project's images.
- [Django](https://www.djangoproject.com/)
  - Django was used to build the app.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/overview.html/)
  - Django allauth for account management.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
  - Django Crispy Forms for rendering elegant DRY forms.
- [Font Awesome](https://fontawesome.com/)
  - Font Awesome was used to add icons to improve the design of the website.
- [Git](https://git-scm.com/) & [Gitpod](https://gitpod.io/)
  - Git was used for version control via the Gitpod terminal in order to commit to Git and push to GitHub.
- [GitHub](https://github.com/)
  - GitHub was used for version control.
- [Google Fonts](https://fonts.google.com/)
  - Google Fonts was used to import the fonts which are used on the website.
- [Heroku](https://heroku.com/)
  - Heroku was used for hosting and deploying the game.
- [PostgreSQL](https://www.postgresql.org/)
  - PostgreSQL for database management.
- [Summernote](https://summernote.org/)
  - Summernote WYSIWYG for Bootstrap.

## Testing

### Testing User Stories from User Experience (UX) Section

- 

### Validator Testing

- 

### Google Lighthouse

- 

### Color Contrast Accessibility Checker

- 

### Responsive Testing

- 

### Device Testing

- 
  - 

### Browser Testing

- 

### Fixed Bugs

- 

## Deployment

- 

## Credits 

### Content

- 

### Media

- 

### Other

- Many thanks to my mentor, Gerry McBride, for his guidance and feedback.