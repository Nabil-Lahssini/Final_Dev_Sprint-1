<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

<<<<<<< HEAD

Route::get('/', function () {
    return view('home');
});
=======
Route::get('/', function () {
    return view('home');
});

Route::get('/profile', function () {
    return view('profile');
});
>>>>>>> e4a10ca1317cbd6690459d9e1778d2b3b8d3fc8f

Auth::routes();

Route::get('/apointment', [App\Http\Controllers\ApointmentController::class, 'index'])->name('apointment.index');
