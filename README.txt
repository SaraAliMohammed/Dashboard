***open cmd

-make directory using -> mkdir DataCenterProject
	-move to the new directory -> cd DataCenterProject
	-run this command -> virtualenv venv-DataCenter
	-run the script -> D:\Work\Tasks\Task7\DataCenterProject\venv-DataCenter\Scripts\activate
	-To make new project run this command -> django-admin.py startproject DataCenterProject
	-move to the  projectFolder -> cd DataCenterProject
	-run this command 'you can change port number' -> python manage.py runserver 8080
	-go to the given url
	-To Create app -> python manage.py startapp blogs
	--add the app in settings.py at installedApps-> 'blogs'

***To create super user to manage project with development team-> 
	-run this command -> python manage.py migrate
	-run this command -> python manage.py createsuperuser
	-Create username and password --> name : datacenter , pass : D@tacenter
	-run this command -> python manage.py runserver 8080
	-go to http://127.0.0.1:8080/admin/login/?next=/admin/
	-enter user and password

***app
	-r.c on blogs -> new directory -> templates
	-r.c on templates -> new file -> dataCenter.html
	-add function on views.py -> from django.shortcuts import render_to_response
				     def dataCenterView(request):
    					return render_to_response('dataCenter.html')

	

	-To add its url go to urls.py on urlpatterns ->  url(r'^$', 'blogs.views.login', name='login'),

	
	-In models add:
		
	-Then Run -> cd /path
		  -> python manage.py makemigrations
		  -> python manage.py migrate
	-To add the app to the admin page go to  the admin.py 
	-> from .models import Server,Mac
	-> admin.site.register(Server)

	-To view all details on admin.py 
		-> class ServerAdmin(admin.ModelAdmin):
    			list_display = [ "Type" , "RAM" , "Core" , "Storage" ]
    			class Meta:
        			model=Server

		-> class MacAdmin(admin.ModelAdmin):
    			list_display = ["ServerID" , "MacNum"]
    			class Meta:
        			model=Mac

	-> admin.site.register(Server,ServerAdmin)
	   admin.site.register(Mac,MacAdmin)

***To add css,img
	-add in settings.py -> 	STATIC_URL = '/static/'

				STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_in_env","static_root")

				STATICFILES_DIRS = [
    					os.path.join(BASE_DIR, "static_in_pro","our_static"),
				]
	-create static_in_pro folder and inside it create our_static folder
	-create static_in_env folder and inside it create static_root folder
	-to test only move files to static_root -> run the following command -> python manage.py collectstatic
***Add imports to urls.py -> 
	-from django.conf import settings
	-from django.conf.urls.static import static
	-beside urlpatterns add -> 
		if settings.DEBUG:
    			urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
