# Editing the ICMNS website

This guide is for organisers and committee members who want to update [icmns.org](https://icmns.org). You do not need to install anything: every common task can be done in your browser on github.com.

**How it works in one sentence:** the website is a set of text files in this repository; when a change is saved ("committed") to the `main` branch, GitHub rebuilds the site and publishes it at icmns.org within about two minutes.

---

## 1. Getting access

1. Create a free account at [github.com](https://github.com) if you don't have one.
2. Ask one of the current maintainers to invite you to the [`icmns-org`](https://github.com/icmns-org) organisation. You will get an email; accept the invitation.
3. You can now edit files in the [website repository](https://github.com/icmns-org/icmns-org.github.io).

---

## 2. Editing a page on github.com

1. Go to the [repository](https://github.com/icmns-org/icmns-org.github.io) and click the file you want to change (see [where things are](#3-where-things-are)).
2. Click the **pencil icon** (✏️ "Edit this file") at the top right of the file.
3. Make your changes. Use the **Preview** tab to check formatting.
4. Click **Commit changes…** (green button). Write a short description, e.g. *"Add 2027 keynote speakers"*.
5. Choose one of:
   - **Commit directly to the `main` branch**: for small, safe edits (typos, dates, a news post). The change goes live in about two minutes.
   - **Create a new branch and start a pull request**: for larger changes, or if you'd like someone to check your work first. Another maintainer reviews it and clicks *Merge*; only then does it go live.
6. Check that it worked: see [section 6](#6-checking-your-change-went-live).

**To add a new file** (e.g. a news post): open the folder, click **Add file → Create new file**, type the file name, write the content, and commit as above.

**To upload an image or PDF:** open the `assets/images` folder (or type `assets/images/` in the file name box to create it), click **Add file → Upload files**, drag the file in and commit.

---

## 3. Where things are

| What you see on the site | File to edit |
|---|---|
| Home page (logo, next edition, buttons) | `index.md`; the next edition's name, dates and location come from its file in `_editions/` |
| News posts | `_posts/` (one file per post) |
| About page (history, steering committee) | `about.md` |
| A conference edition, e.g. icmns.org/2025/ | `_editions/2025.md` |
| The Past editions table | Built automatically from `_editions/`; don't edit `editions.md` for content |
| Menu at the top | `_data/navigation.yml` |
| Contact email, site title, current edition year | `_config.yml` |
| Colours and layout | `assets/css/style.css` |
| Page templates (header, footer) | `_layouts/` (rarely needed) |

---

## 4. Common tasks

### Post a news item

Create a new file in `_posts/` named with the date and a short title, all lowercase with hyphens:

```
_posts/2026-11-05-registration-open.md
```

Content:

```markdown
---
title: Registration for ICMNS 2027 is open
---
Registration is now open for ICMNS 2027 in ... Early-bird rates apply until ...

[Register here](https://example.org/registration).
```

The post appears on the [News page](https://icmns.org/news/), in the "Latest news" box on the home page and in the news feed. The **first paragraph** is used as the summary, so make it a complete sentence. A file dated in the future is not published until that date has passed and the site is rebuilt.

### Update the key dates

The **Key dates** table on an edition page (e.g. `_editions/2027.md`) is filled from the list `key_dates` in the part between the two `---` lines. Replace `TBA` with the date, written as year-month-day:

```yaml
key_dates:
  - milestone: Abstract submission opens
    date: 2027-01-15
    until: 2027-03-01      # optional: when the window closes
    kind: window
  - milestone: Abstract deadline
    date: 2027-03-01
  - milestone: Conference
    date: 2027-06-01
    until: 2027-06-04
    label: 1–4 June 2027   # optional: text to show instead of the date
    kind: event
```

The **Status** column fills itself in from today's date: *Upcoming*, *Closes soon* (in the last three weeks before a deadline), *Open* / *Under way*, and *Closed* / *Done*. The site rebuilds every night, so the statuses stay current. `kind` is `deadline` if you leave it out.

The home page is deliberately minimal: it shows the logo and the next edition's dates and location, which it reads from the edition file, so there is usually nothing to edit in `index.md`.

### Add details to the upcoming edition

Edit `_editions/2027.md` (or the relevant year). The part between the two `---` lines is the summary used across the site:

```yaml
---
year: 2027
edition: 12th
dates: 7–10 June 2027
location: City, Country
venue: Name of the venue
links:
  - title: Registration
    url: https://...
---
```

Below the second `---`, write the page in Markdown: speakers, committees, programme, travel information. Each `## Heading` becomes a numbered section, with the heading on the left and its text on the right. For a list of people, write the name in bold and the affiliation on the next line, indented by two spaces:

```markdown
- **Alain Goriely**
  University of Oxford, UK
```

Write the plenary speakers like this; other lists can stay as plain bullets. Look at `_editions/2024.md` or `_editions/2025.md` for a complete example to copy.

### Start a new edition (once a year)

1. Open the latest edition file (e.g. `_editions/2027.md`), copy its content.
2. Create `_editions/2028.md` with that content and update the year, dates and location.
3. In `_config.yml`, change `current_edition: 2027` to `current_edition: 2028`. The home page now shows 2028, and 2027 moves to *Past editions* automatically.

### Change the menu

Edit `_data/navigation.yml`. Each entry is two lines; keep the indentation exactly as it is:

```yaml
- title: News
  url: /news/
```

### Link to another page or file

```markdown
[ICMNS 2025](/2025/)
[Programme (PDF)](/assets/images/programme-2027.pdf)
[External site](https://www.crm.cat/)
```

### Add an image

Upload the image to `assets/images/` (see [section 2](#2-editing-a-page-on-githubcom)), then:

```markdown
![Participants at ICMNS 2025 in Barcelona](/assets/images/icmns2025-group.jpg)
```

Keep images under about 1 MB (resize photos to about 1600 px wide). Make sure you have permission to publish them.

### Write mathematics

Equations are typeset by LaTeX in IBM Plex Mono Italic and shown as images in the text colour. Add `math: true` to the page's header and write each formula between **double** dollar signs; a formula on a line of its own is centred:

```markdown
---
title: ...
math: true
---
The membrane potential obeys $$\tau \dot V = -V + I(t)$$, and

$$ \frac{\partial u}{\partial t} = -u + \int w(x-y)\, f(u(y,t))\, dy. $$
```

Then, on a computer with LaTeX installed (MacTeX or TeX Live), run

```sh
python3 tools/render_maths.py
```

and commit the new files it creates in `_maths/`. Until you do, the formula appears on the site as red LaTeX code, and the build log says which formula is missing. Editing on github.com alone is therefore not enough for maths: ask a maintainer to run the script if you can't.

---
title: ...
math: true
---
The membrane potential obeys $\tau \dot V = -V + I(t)$, and

$$ \frac{\partial u}{\partial t} = -u + \int w(x-y)\, f(u(y,t))\, dy. $$
```

---

## 5. Markdown in two minutes

| You write | You get |
|---|---|
| `## Heading` | A section heading |
| `**bold**`, `*italic*` | **bold**, *italic* |
| `[text](https://...)` | A link |
| `- item` (one per line) | A bullet list |
| `1. item` | A numbered list |
| A blank line | A new paragraph |
| `<!-- note -->` | A hidden comment (not shown on the site) |

**The header between `---` lines** (the "front matter") needs care:
- Keep both `---` lines.
- Write `key: value`, with a space after the colon.
- If a value contains a colon, put it in quotes: `title: "ICMNS 2027: call for papers"`.
- Use spaces, never tabs, for indentation.

---

## 6. Checking your change went live

1. In the repository, open the **Actions** tab. Your change appears at the top:
   - 🟡 yellow dot: building (about one minute);
   - ✅ green tick: published, refresh icmns.org to see it;
   - ❌ red cross: the build failed and **the live site is unchanged**.
2. If it failed, click the run, then the red step, to see the error. It usually names the file and line, and is almost always a problem in the `---` header (a missing space, an unquoted colon, a tab).
3. Fix the file and commit again, or undo your change: open the file, click **History**, open your commit, and use **Revert** (or ask a maintainer).

If the site looks unchanged after a green tick, force-refresh your browser (Cmd+Shift+R on Mac, Ctrl+F5 on Windows).

---

## 7. Please don't

- **Delete or edit `CNAME`**: it connects the site to icmns.org.
- **Edit `.github/workflows/`, `Gemfile` or `Gemfile.lock`** unless you know what they do: they control how the site is built.
- **Upload large files** (videos, files over about 10 MB). Link to YouTube, Zenodo or a cloud folder instead.
- **Publish personal data** (private emails, phone numbers) without consent, or anything confidential: this repository is public, and so is its full history.

---

## 8. Previewing locally (optional, for regular contributors)

If you prefer working in a text editor and seeing changes before publishing:

1. Install [Git](https://git-scm.com) and Ruby 3 (macOS: `brew install ruby`; then follow the instructions it prints to add it to your `PATH`).
2. Clone the repository and start the preview:

   ```sh
   git clone https://github.com/icmns-org/icmns-org.github.io.git
   cd icmns-org.github.io
   bundle config set --local path vendor/bundle
   bundle install
   bundle exec jekyll serve --livereload
   ```

3. Open <http://localhost:4000>. The page reloads every time you save a file.
4. When you're happy: `git add -A`, `git commit -m "Describe your change"`, `git push`.

---

## Questions

Ask one of the website maintainers, or open an [issue](https://github.com/icmns-org/icmns-org.github.io/issues) describing what you'd like to change.
