import requests

class APIClient(object):
    '''
    Real api client for retrieving sudoku puzzles.
    
    The Sudoku API will only allow one request every three minutes, and
    up to 500 each day from any one IP address. Additionally, users must
    have a valid username / key combo or no puzzle will be returned.

    The server starts with 50,000 unique puzzles. Each time the API is 
    accessed, a puzzle is removed from the database and sent to the requesting
    computer. Once a puzzle is removed, there is no way to retrieve it a 
    second time. Because of this, it is imperative that you are certain that
    your pipeline is saving the puzzles securely. 

    To test your requests, set the username to 'Test'. This will cause the api
    to return a test string without removing any puzzles from the database. I 
    suggest making sure you can automate saving the test string on your local
    machine before running the API with your name and key.
    '''

    def __init__(self, user_name='Test', api_key=None, address='http://127.0.0.1:5000/sudoku_api'):
        # While these attributes can be changed after instantiation,
        # we generally would not access them. This is indicated by the 
        # name starting with an underscore.
        self._name = user_name
        self._key = api_key
        self._url = address

    def get_puzzle(self):
        '''The requests module allows your Python script to request information
        from websites. A company with an API will often require users to provide
        additional parameters on the address bar when accessing the API.'''

        # In this case, we are using only two parameters: name and key
        return requests.get(f'{self._url}?name={self._name}&key={self._key}')

    def run_time(self):
        ''' You will not be able to access every puzzle manually, one at a time 
        because it would take too much time. (There are 50,000 of them!) 
        Instead, you will need to automate the API request process by developing
        a pipline. Use this run_time method to automatically pull
        a new puzzle every 3 minutes. Make sure you have completed the 
        save_puzzle method first before running! '''

        # Here is some sudo-code to get you going:

        # get puzzle from self.get_puzzle()
        # use self.save_puzzle() to save the puzzle to memory
        # wait 3 minutes (or longer?) using Python's time module
        # run self.run_time() again

        # Extra Credit, have this method:
        # 1) wait for a longer period of time if you have reached your daily limit.
        # 2) stop automatically if there are no more puzzles.
        # 
        # (When there are no more puzzles, the API will return the string:
        # 'There are no more puzzles!')
        pass

    def solve_puzzle(self, puzzle):
        '''
        Data Pipelines, also sometimes called ETL for Extract, Transform, and Load;
        have three parts. First you must get the data, and at the end you must
        save it. But in between those two steps is a wildly explorative stage
        of data manipulation. 

        For this problem, we will be turning sudoku problems into their solutions.
        You can write your sudoku solver code here, or if you want more room 
        you can write it on a new script and import it.
        '''
        pass


    def save_puzzle(self, puzzle):
        '''This method should save puzzles to your local machine. You will 
        probably want to start saving puzzles from the API as soon as 
        possible, to ensure that you are able to acquire all of them before
        the end of the assignment. The easiest way to do this is to write add
        each puzzle to a csv file.
        
        Once you are done with the solve_puzzle method, you can create a 
        new csv with both puzzle and answer together on one line separated 
        by a comma. I have included an example csv in the data folder, with
        three puzzles and their solutions.'''
        pass
        

if __name__ == "__main__":
    pass
    # # Store your unique api name and key here, or use name = Test for testing:
    # user_name = 'Test'
    # api_key = None

    # # Creating a client for accessing the api database.
    # client = APIClient(user_name, api_key)

    # # Acquiring a puzzle from the client. 
    # # The puzzle is returned as part of a Response object. Try calling
    # # dir(response) to see what attributes it has. 
    # # HINT: The puzzle is formatted as a string.
    # response = client.get_puzzle()