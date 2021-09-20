import requests


monthNames = [
  "January", "February", "March", "April", "May", "June", "July", 
  "August", "September", "October", "November", "December" ]


class github_api():

    def make_request(self, username):
        '''
        Returns the a list of all the repos of the spcified user.

            Parameters:
                    self: An object of a class
                    username (string): the username of the github user

            Returns:
                    a list of all the repost that belongs to the specified user
        '''
        
        if username != "":
            try:
                url = 'https://api.github.com/users/'+str(username)+'/repos'
                responses = requests.get(str(url))
                responses = responses.json()
                return responses
            except Exception as exp:
                print(exp)
        else:
            print("Username is empty please spcify a username")