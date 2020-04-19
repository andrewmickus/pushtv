from flask import Flask, render_template
import boto3
import random

base_url = 'https://pushtv.s3-us-west-2.amazonaws.com/'

def get_buckets():
	s3_resource = boto3.resource('s3')

	urls = []
	
	for bucket in s3_resource.Bucket('pushtv').objects.filter(Prefix='tv'):
	     urls.append('{0}'.format(bucket.key))
	return urls

	
application = Flask(__name__)

@application.route('/')
def home():
	return("i'm the main page.")

@application.route('/<tv>')
def show_pic(tv):

	urls = get_buckets()

	tvs = [url.replace("/","") for url in urls if url.endswith("/")]        
	pic_urls = [base_url + url for url in urls if not url.endswith("/")]

	return render_template("main.html", displayed_image = random.choice([x for x in pic_urls if tv in x]))

if __name__ == "__main__":
	application.run(debug=True)