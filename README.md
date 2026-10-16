# icmns.org

Source for the website of the International Conference on Mathematical Neuroscience,
built with [Jekyll](https://jekyllrb.com) and deployed to GitHub Pages on every push to `main`.

## Editing

**New contributors: see [CONTRIBUTING.md](CONTRIBUTING.md) for a step-by-step guide to editing the site on github.com.**

- Pages are Markdown files in the repo root (`index.md`, `about.md`, ...). Edit them directly on github.com.
- Each conference edition is a file in `_editions/` (e.g. `_editions/2027.md`) and appears at `icmns.org/2027/`.
- To start a new edition: copy the previous file, update the front matter, and set `current_edition` in `_config.yml`.
- News posts are files in `_posts/` named `YYYY-MM-DD-short-title.md`, starting with:

      ---
      title: Your headline
      ---

  They appear on `/news/`, in the "Latest news" box on the home page and in the feed (`/feed.xml`). The first paragraph is used as the excerpt.
- Menu entries live in `_data/navigation.yml`.
- Add `math: true` to a page's front matter to enable LaTeX via MathJax.

## Local preview

Requires Ruby 3.x (`brew install ruby`), then:

    bundle install
    bundle exec jekyll serve

and open http://localhost:4000.
