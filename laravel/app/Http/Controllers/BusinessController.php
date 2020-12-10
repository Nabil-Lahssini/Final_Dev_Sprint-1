<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BusinessController extends Controller
{
    //
    public function index()
    {
        return view('business.addBusiness');
    }

    public function store()
    {

        $data=request()->validate([
            'nameBusiness'=>'required|max:255',
            'typeBusiness'=>'required|max:255',
            'appointmentTimeBusiness'=>'required',
            'phoneBusiness'=>'required|size:10',
            'emailBusiness'=>'required|max:255',
            'streetBusiness'=>'required|max:255',
            'houseNumberBusiness'=>'required|max:255',
            'cityBusiness'=>'required|max:255',
            'postalcodeBusiness'=>'required|max:255',
            'countryBusiness'=>'required'

        ]);

        //API Url
$url = 'http://example.com/api/JSON/create';
 
//Initiate cURL.
$ch = curl_init($url);
 
//The JSON data.
$jsonData = array(
    'business_type' => $data["typeBusiness"],
    'name' => $data["nameBusiness"],
    'appointment_time' => $data["appointmentTimeBusiness"],
    'country' => $data["countryBusiness"],
    'city' => $data["cityBusiness"],
    'code' => $data["postalcodeBusiness"],
    'street' => $data["streetBusiness"],
    'house_nr' => $data["houseNumberBusiness"],
    'email' => $data["emailBusiness"],
    'phone' => $data["phoneBusiness"],
    'id_owner' => '3'
    
);
 
//Encode the array into JSON.
$jsonDataEncoded = json_encode($jsonData);
 
//Tell cURL that we want to send a POST request.
curl_setopt($ch, CURLOPT_POST, 1);
 
//Attach our encoded JSON string to the POST fields.
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonDataEncoded);
 
//Set the content type to application/json
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json')); 
 
//Execute the request
$result = curl_exec($ch);

                    
    }



}
