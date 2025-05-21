from flask import Flask, render_template, request , url_for
from werkzeug.utils import redirect

app = Flask(__name__)


Destinations =("UK","Australia","France","Indonesia","Italy","Japan")

bookings = [
    {"bookingid":1,"name":"Abram Qureshi","flightno":"FB1001","Destination":"Australia","price":5000},
    {"bookingid":2,"name":"Bob","flightno":"FB1002","Destination":"UK","price":6000}

]

bookingid ={1,2}

@app.route("/")
def home():
    return render_template("index.html",destinations = Destinations, bookings = bookings)


@app.route("/addbooking", methods = ["POST","GET"])
def addBooking():

    if request.method == "POST":

        bid= (max(bookingid)+1) if bookings else 1
        name= request.form["name"]
        flightnumber=request.form["flightno"]
        dest=request.form["destination"]
        price = request.form["price"]
        bookingid.add(bid)
        newbooking = {"bookingid":bid,"name":name,"flightno":flightnumber,"Destination":dest,"price":price}
        bookings.append(newbooking)

        return redirect(url_for("home"))
    return render_template("addbooking.html",bookings =bookings, destinations = Destinations)

@app.route("/editbooking/<id>", methods =["POST", "GET"])
def editbooking(id):
    booking = next((b for b in bookings if b["bookingid"]==int(id)),None)
    if request.method == "POST":

        booking["name"] = request.form["name"]
        booking["flightno"] = request.form["flightno"]
        booking["Destination"] = request.form["destination"]
        booking["price"] = request.form["price"]
        return redirect(url_for("home"))
    return render_template("edit.html",booking =booking, destinations = Destinations)

@app.route("/deletebooking/<id>",methods = ["POST","GET"])
def deletebooking(id):
    for booking in bookings:
        if booking["bookingid"] == int(id):
            bookings.remove(booking)
            break

    bookingid.remove(int(id))
    return redirect(url_for("home"))


if __name__ == "__main__" :
    app.run(debug=True)
