import bs4
import gtts

def extract_stories_from_NPR_text(text):
    '''
    Extract a list of stories from the text of the npr.com webpage.

    @params: 
    text (string): the text of a webpage

    @returns:
    stories (list of tuples of strings): a list of the news stories in the web page.
      Each story should be a tuple of (title, teaser), where the title and teaser are
      both strings.  If the story has no teaser, its teaser should be an empty string.
    '''
    soup = bs4.BeautifulSoup(text, 'html.parser')
    stories = []

    # Find all story elements (adjust selector based on the NPR website structure)
    for story in soup.find_all('article'):  # Assuming stories are wrapped in <article>
        title_tag = story.find('h2')  # Assuming titles are in <h2> tags
        teaser_tag = story.find('p')  # Assuming teasers are in <p> tags

        title = title_tag.get_text(strip=True) if title_tag else ""
        teaser = teaser_tag.get_text(strip=True) if teaser_tag else ""

        if title:  # Only include stories with a title
            stories.append((title, teaser))

    return stories

def read_nth_story(stories, n, filename):
    '''
    Read the n'th story from a list of stories.

    @params:
    stories (list of tuples of strings): a list of the news stories from a web page
    n (int): the index of the story you want me to read
    filename (str): filename in which to store the synthesized audio

    Output: None
    '''
    if not 0 <= n < len(stories):
        raise IndexError("Story index out of range.")

    title, teaser = stories[n]
    text_to_read = f"Title: {title}\nTeaser: {teaser}" if teaser else f"Title: {title}"

    tts = gtts.gTTS(text_to_read)
    tts.save(filename)
    print(f"The {n}th story has been saved as {filename}.")
