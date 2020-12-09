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

=======
Route::get('/', function () {
    return view('home');
});
>>>>>>> f47ac079494430676bb8e78664f481befef59a8f

Auth::routes();

Route::get('/apointment', [App\Http\Controllers\ApointmentController::class, 'index'])->name('apointment.index');
