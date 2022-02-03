from modules import app, db
from os.path import join, dirname
from dotenv import load_dotenv
import os





dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class GetData():

    def get_reviews(self):
        my_reviews = list(db.child('Reviews').get().val().values())
        my_reviews.reverse()
        return my_reviews

    def get_messages(self):
        my_messages = list(db.child('Contact-Us').get().val().values())
        my_messages.reverse()
        return my_messages

    def get_numbers(self):
        return {
            'totalReviews' : len(db.child('Reviews').get().val()),
            'totalMessages' : 0 if isinstance(db.child('Contact-Us').get().val(), type(None)) else len(db.child('Contact-Us').get().val()),
            'instagram' : sum(
                i['Instagram'] == 1 for i in list(db.child('Reviews').get().val().values())
            )
        }




class NavbarActive():
    home = False
    table = False
    write = False
    message = False

    def set_home(self):
        self.home = True
    def set_table(self):
        self.table = True
    def set_write(self):
        self.write = True
    def set_message(self):
        self.message = True



def bool2binary(arg):
    if arg:
        return 1
    return 0



def save_poster(form_pic):
    f_name,f_ext = os.path.splitext(form_pic.filename)
    picture_fn = f_name + f_ext
    picture_path = os.path.join(app.root_path, 'Extra/Images', picture_fn)
    form_pic.save(picture_path)
    return print('Saved to Static/img')



def remove_img(path, img_name):
    os.remove(path + '/' + img_name)
    if os.path.exists(path + '/' + img_name) is False:
        return True


def return_node(id,database, prop, nodeValue=False):
    if nodeValue:
        return [[rev.key(), rev.val()] for rev in db.child(database).get().each() if rev.val()[prop] == id]
    return [rev.key() for rev in db.child(database).get().each() if rev.val()[prop] == id]