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
            'nameBusiness'=>'required',
            'typeBusiness'=>'required',
            'phoneBusiness'=>'required',
            'emailBusiness'=>'required',
            'streetBusiness'=>'required',
            'houseNumberBusiness'=>'required',
            'cityBusiness'=>'required',
            'postalcodeBusiness'=>'required',
            'countryBusiness'=>'required'

        ]);
    }
}
