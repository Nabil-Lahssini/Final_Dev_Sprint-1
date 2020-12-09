<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ApointmentController extends Controller
{
    public function index(){
        return view('apointment.index');
    }
}
