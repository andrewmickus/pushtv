from flask import Flask, render_template
import boto3

#s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

#pushtv_bucket = s3_resource.Bucket('pushtv/tv1/').objects


for bucket in s3_resource.buckets.all():
    for obj in bucket.objects.filter(Prefix='tv1/'):
        print('{0}'.format(obj.key))


#"https://pushtv.s3-us-west-2.amazonaws.com/tv1/asian_box_default.jpeg"


#for bucket in s3_resource.buckets.all():
#        print(bucket.name)


#for key in conn.list_objects(Bucket='bucket_name')['Contents']:
#    print(key['Key'])


#app = Flask(__name__)

#@app.route('/')

#def home():
	#return render_template("main.html")

#if __name__ == "__main__":
#	app.run(debug=True)