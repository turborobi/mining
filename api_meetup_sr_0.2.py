import urllib, json, time

#### Version 0.1 ####
##
## Rate limits as per Meetup:
#X-RateLimit-Limit: 30
#X-RateLimit-Remaining: 29
#X-RateLimit-Reset: 10
#X-OAuth-Scopes: basic
########################################################
#CODE TODO:
# - break down in classes 
# - option to export to tab-separated file (os module)
# - Catch URL open errors with TRY ...
# - rate-limit if needed (time.sleep)
# - more fields to extract as needed? 
# - tidy up code, more comments, help on module
# - upgrade code to python 3 ... and get rid of unicode issues!
#########################################################


print 'You can get your API key at https://secure.meetup.com/meetup_api/key/  (login required)'
print
secret_api_key = raw_input('What is your API Key? (required) ')
print

api_url_with_key = 'https://api.meetup.com/2/members?key='+secret_api_key+'&group_id=22102008'

# open URL and unpack JSON with JSON module
member_list = urllib.urlopen(api_url_with_key)
member_list_json = json.load(member_list)

# number of keys (members)
number_of_members = len(member_list_json['results'])

#Unpack the list of members
for i in range(number_of_members):

    # Short pause to slow down process and not get kicked out
    #time.sleep(3)

    ## Extract the member ID
    member_id = member_list_json['results'][i]['id']

    ## Extract the member NAME
    member_name = member_list_json['results'][i]['name']

    ## no need to print name... TEST only
    ## print ('----> The member name is:  ', member_name)

    url_for_member_info = 'https://api.meetup.com/groups?key='+secret_api_key+'&member_id=' + str(member_id)

    try:    member_info = urllib.urlopen(url_for_member_info)
    except IOError as e:
        print unicode(member_name), '\t', member_id , '\t' , unicode('**_NO_PUBLIC_GROUPS_**')
        continue

    member_info_json = json.load(member_info)

    # initialize counter to iterate through groups
    counter = 0

    # Extracting the member's groups where he/she belongs
    for group in member_info_json['results'][:]:

        extracted_group = member_info_json['results'][counter]['name']

        print unicode(member_name), '\t', member_id , '\t' , unicode(extracted_group)

        counter += 1
    
    
    
     
