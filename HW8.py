# Your name: Jackson Gertner
# Your student id: 3536 9924
# Your email: jgertner@umich.edu
# List who you have worked with on this homework: Amelia Learner Jackson Gelbard

import matplotlib.pyplot as plt
import os
import sqlite3
import unittest

def load_rest_data(db):
    path = os.path.dirname(os.path.abspath(__file__))

    conn = sqlite3.connect(path + '/' + db)

    cur = conn.cursor()

    cur.execute("SELECT restaurants.name, restaurants.building_id, restaurants.rating, restaurants.category_id, buildings.id, buildings.building, categories.id, categories.category FROM restaurants INNER JOIN buildings ON restaurants.building_id = buildings.id INNER JOIN categories ON restaurants.category_id = categories.id")

    rows = cur.fetchall()

    d = {}

    for restaurant in rows:

        name = restaurant[0]

        category = restaurant[7]

        building = restaurant[5]

        rating = restaurant[2]

        d[name] = {"category": category, "building": building, "rating": rating}

        conn.close()

    return d

def plot_rest_categories(db):
    path = os.path.dirname(os.path.abspath(__file__))

    conn = sqlite3.connect(path + '/' + db)

    cur = conn.cursor()



    cur.execute("SELECT restaurants.name, restaurants.building_id, restaurants.rating, restaurants.category_id, buildings.id, buildings.building, categories.id, categories.category FROM restaurants INNER JOIN buildings ON restaurants.building_id = buildings.id INNER JOIN categories ON restaurants.category_id = categories.id")

    rows = cur.fetchall()



    cat_count = {}

    for row in rows:
        category = row[7]
        if category not in cat_count:
            cat_count[category] = 1
        else:
            cat_count[category] += 1
    categories = cat_count.keys()

    counts = cat_count.values()



    plt.bar(categories, counts)

    plt.xlabel('Restaurant Categories')

    plt.ylabel('Number of Restaurants per Category')

    plt.title('Restaurant Category Counts')

    plt.xticks(rotation=90)

    plt.show()



    conn.close()

    return cat_count

def find_rest_in_building(building_num, db):
    path = os.path.dirname(os.path.abspath(__file__))

    conn = sqlite3.connect(path + '/' + db)

    cur = conn.cursor()



    cur.execute("SELECT restaurants.name, restaurants.building_id, restaurants.rating, restaurants.category_id, buildings.id, buildings.building, categories.id, categories.category FROM restaurants INNER JOIN buildings ON restaurants.building_id = buildings.id INNER JOIN categories ON restaurants.category_id = categories.id")

    rows = cur.fetchall()



    names_rev = []



    for restaurant in rows:

        if restaurant[5] == building_num:

            tup = (restaurant[0], restaurant[2])

            names_rev.append(tup)



            names_rev.sort(key = lambda x: x[1], reverse = True)

            final_lst = []

    for res in names_rev:

        final_lst.append(res[0])

    return final_lst

#EXTRA CREDIT
def get_highest_rating(db): #Do this through DB as well
    """
    This function return a list of two tuples. The first tuple contains the highest-rated restaurant category 
    and the average rating of the restaurants in that category, and the second tuple contains the building number 
    which has the highest rating of restaurants and its average rating.

    This function should also plot two barcharts in one figure. The first bar chart displays the categories 
    along the y-axis and their ratings along the x-axis in descending order (by rating).
    The second bar chart displays the buildings along the y-axis and their ratings along the x-axis 
    in descending order (by rating).
    """
    pass

#Try calling your functions here
def main():
    pass

class TestHW8(unittest.TestCase):
    def setUp(self):
        self.rest_dict = {
            'category': 'Cafe',
            'building': 1101,
            'rating': 3.8
        }
        self.cat_dict = {
            'Asian Cuisine ': 2,
            'Bar': 4,
            'Bubble Tea Shop': 2,
            'Cafe': 3,
            'Cookie Shop': 1,
            'Deli': 1,
            'Japanese Restaurant': 1,
            'Juice Shop': 1,
            'Korean Restaurant': 2,
            'Mediterranean Restaurant': 1,
            'Mexican Restaurant': 2,
            'Pizzeria': 2,
            'Sandwich Shop': 2,
            'Thai Restaurant': 1
        }
        self.highest_rating = [('Deli', 4.6), (1335, 4.8)]

    def test_load_rest_data(self):
        rest_data = load_rest_data('South_U_Restaurants.db')
        self.assertIsInstance(rest_data, dict)
        self.assertEqual(rest_data['M-36 Coffee Roasters Cafe'], self.rest_dict)
        self.assertEqual(len(rest_data), 25)

    def test_plot_rest_categories(self):
        cat_data = plot_rest_categories('South_U_Restaurants.db')
        self.assertIsInstance(cat_data, dict)
        self.assertEqual(cat_data, self.cat_dict)
        self.assertEqual(len(cat_data), 14)

    def test_find_rest_in_building(self):
        restaurant_list = find_rest_in_building(1140, 'South_U_Restaurants.db')
        self.assertIsInstance(restaurant_list, list)
        self.assertEqual(len(restaurant_list), 3)
        self.assertEqual(restaurant_list[0], 'BTB Burrito')

    def test_get_highest_rating(self):
        highest_rating = get_highest_rating('South_U_Restaurants.db')
        self.assertEqual(highest_rating, self.highest_rating)

if __name__ == '__main__':
    main()
    unittest.main(verbosity=2)
