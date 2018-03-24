from random import randint


class Quote:
    def __init__(self, quote_id, content, author):
        """
        Quote that is shown on the index page
        """
        self.quote_id = quote_id
        self.content = content
        self.author = author


class QuoteList:
    """
    Quotes list from text file
    """
    def __init__(self):
        with open('my_blog/static/quotes.txt', 'r') as f:
            self.quote_list = [x for x in f.readlines() if len(x) > 1]

    def random_quote(self):
        """
        Returns random quote selected from text file
        :return: random quote
        """
        q = self.quote_list[randint(1, 100)]
        random_quote = Quote(quote_id=q[:q.find('.')],
                             content=q[(q.find('.') + 2):q.find('~')],
                             author=q[q.find('~')+1:])
        return random_quote


quote_list = QuoteList()
