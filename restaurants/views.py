from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { 
		
		"my_list": [
			{
			"restaurant_name" : "kfc",
			 "food_type" : "chicken"
			},
			{
				"restaurant_name" : "mcdonalds",
				"food_type" : "fast"
			},
			{
				"restaurant_name": "dominos",
				"food_type": "pizza"
			}
		]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { 
		
		"my_object":
			{
			"restaurant_name" : "kfc",
			 	"food_type" : "chicken" 
			 }
	
	}
    return render(request, 'detail.html', context)
