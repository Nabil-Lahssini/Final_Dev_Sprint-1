<?php

namespace App\Http\Controllers;

use App\Models\Calendar;
use Illuminate\Http\Request;

class CalendarController extends Controller
{
    public function create(){
        return view('create');
    }
    public function store(){
        $data=request()->validate([
            'start'=>'required',
            'end'=>'required',
            'title'=>'required',
            'description'=>'required'
        ]);
        Calendar::create($data);
        return redirect('/profile');
    }
}
