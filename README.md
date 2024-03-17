# py-ssg: A Simple Static Site Generator in Python

`py-ssg` is a lightweight static site generator written in Python. It is designed to convert markdown files in the `content` directory into HTML files in the `public` directory. It also copies the contents of the `static` directory into the `public` directory.

## Features

- Converts markdown files to HTML
- Copies static files to the public directory
- Generates a website with a consistent layout
- Supports markdown features like headings, paragraphs, lists, code blocks, and quotes

## Usage

1. Write your content in markdown format and save it in the `content` directory.
2. Place your static files (like images and CSS files) in the `static` directory.
3. Run the `main.sh` script to generate the website:

```sh
./main.sh
```

This will delete the existing public directory, copy the static files to a new public directory, and convert the markdown files to HTML.

## Testing

Run the `test.sh` script:

```sh
./test.sh
```
