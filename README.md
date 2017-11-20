# AlgorithmsMJ - Learning with Algorithms

![AlgoMJ screenshot](algomj-screenshot.png "Screenshot of AlgorithmsMJ homepage")

## Under maintenance -> Will be back up shortly. 

## What is it?
Algorithmsmj allows you to generate a random dataset and then sort it using some of the popular sorting algorithms. When you run sort on the dataset you will also get a time value letting you know how long it took to execute the sort. You can use this to see how different sorting algorithms take a longer or shorter time to execute for the same dataset.  

Additionally there is an about page that describes in detail how the website was built using various technology pieces coordination.  

## How does a user use the site?
A user will enter an integer value for the size of the array, click on "Get random array" and then click on one of the various sort buttons available. A user can either enter a small dataset length value or a very large one depending on their preferences. When datasets are very large it will become clear that bubble sort is not nearly as efficient as merge sort or quick sort. 

## How to run this locally?
1. git clone the repository
2. Set up a virtualenv on your machine using "virtualenv <name for virtualenv folder> --no-site-packages"
3. Activate the virtual env, cd into the folder you just created and type "source bin/activate"
4. Install the required packages with "pip install -r requirements.txt" Requirements.txt is in the /requirements folder
5. Run Django server with "python manage.py runserver" You can make this work for external connections with "python manage.py runserver 0.0.0.0:8000"
6. Browse the website in your browser
  
## Ideas for future work
I think it would be cool if we add a couple of more sorts such as radix sort and bucket sort to see how they perform.

