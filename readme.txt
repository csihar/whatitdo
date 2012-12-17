whatitdo
========

what.it.do is a simple, list-driven, Django-based website designed to make it easy to keep track of your favorite media - TV shows, movies, books, games, and music. 

Basic Usage
===========

After creating an account, a user may access one of their five lists (one for each media type) by clicking on the icon bar to the left side of the screen. From there they can add new list items by clicking the [+] icon to the top right, edit existing items by clicking the item's name, and delete an item by clicking the [x] next to its name. 

Most fields for each item besides "Name" are optional and can be set to whatever suits your sorting purposes best - for example, the "Type" field in the Music category may work best as a genre field for one user, but for another may be more useful to mark different formats (CD, vinyl, digital, etc). The "progress" field in TV, Books, and Games is meant to be used as a brief bookmark note: "pg 127", "ep 23", etc., and clicking the "Finished" box adds a checkmark to make it easier to see which items you are currently working on. The "rating" field takes an integer value from 0-100.

The user's homepage allows for the uploading of a user icon (resized to 100x100px), specifying up to three external links (to the user's other profiles, i.e. Facebook, Twitter, personal blog, etc.), as well as modifying their lists' default sorting behavior. Sorting is two-tiered, so, for example, you may want to sort your Books first by "finished last" (placing books you're currently reading at the top), then by "author." A third sorting tier of "name" is always implicit, so books sorted in this way that share an author will still be sorted alphabetically by title. TIP: If each item in a list has a discreet value for "rating", sorting by "rating" makes it easy to quickly produce a Top 10 (or 20, 100, etc) list of your favorites.

Note that all lists and user profiles are visible to the public, but can only be edited by the user who created them. Email addresses are not visible and are only used for password resetting purposes.


DISCLAIMER: what.it.do is open-source, but at present it is not really designed to be reused. You may use the source code for whatever purposes you like if you, but be aware that I was essentially learning Django/Python from scratch while writing what.it.do so you may find much of the code to be rather inelegant, to say the least; use at your own risk. That said, I welcome any suggestions or critiques from more experienced coders!