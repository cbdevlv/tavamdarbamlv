import csv, io
#from django.contrib.auth.decorations import permisions_required
from django.shortcuts import render
from .models import Product, Size, Category
from django.http import HttpResponse

def product_list(request):
    products = Product.objects.all()
    category= Category.objects.all()
    top_level_cats = Category.objects.filter(parent__isnull=True).order_by('name')
    llc = Category.objects.filter(parent__isnull=False).order_by('name')


    return render(request, 'products/product_list.html', {'products':products, 'category':category,
                                        'top_level_cats':top_level_cats,'llc':llc})


def show_category(request,hierarchy= None):
    category_slug = hierarchy.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [ x.slug for x in category_queryset ]
    parent = None
    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(Category,slug=slug,parent=parent)
        else:
            instance = get_object_or_404(Post, slug=slug)
            breadcrumbs_link = instance.get_cat_list()
            category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
            breadcrumbs = zip(breadcrumbs_link, category_name)
            return render(request, "postDetail.html", {'instance':instance,'breadcrumbs':breadcrumbs})

    return render(request,"categories.html",{'post_set':parent.post_set.all(),'sub_categories':parent.children.all()})
