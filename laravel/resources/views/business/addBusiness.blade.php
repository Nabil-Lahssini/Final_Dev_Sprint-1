<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <style>
        

        .addBusinessBtn{
            float: right;
            margin-right: 100px;
            margin-bottom: 20px;
        }


        .addBusinessBox h3{
            margin-left: 40px;
        }

        .addBusinessBox h2{
            text-align: center;
        }

        #countryBusiness:hover{
            cursor: pointer;
        }


    </style>
</head>
<body>
    


@extends('layouts.app')

@section('content')


<div class="container py-5 addBusinessBox">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                

                <div class="card-body">
                    <form action="/Business/create" method="POST">
                        @csrf
                        <br>

                        <h2>Add a Business</h1>

                        <hr>

                        <br>

                        <h3>Business Information</h3>

                        <br>

                        <div class="form-group row">
                            <label for="nameBusiness" class="col-md-4 col-form-label text-md-right">{{ __('Name') }}</label>

                            <div class="col-md-6">
                                <input id="nameBusiness" type="text" placeholder="Name..." class="form-control @error('nameBusiness') is-invalid @enderror" name="nameBusiness" autocomplete="nameBusiness">

                                @error('nameBusiness')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="typeBusiness" class="col-md-4 col-form-label text-md-right">{{ __('Type') }}</label>

                            <div class="col-md-6">

                            <input id="typeBusiness" type="text" placeholder="Type..." class="form-control @error('typeBusiness') is-invalid @enderror" name="typeBusiness"  autocomplete="typeBusiness">

                            @error('typeBusiness')
                            <span class="invalid-feedback" role="alert">
                            <strong>{{ $message }}</strong>
                           </span>
                            @enderror
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="appointmentTimeBusiness" class="col-md-4 col-form-label text-md-right">{{ __('Appointment time') }}</label>

                            <div class="col-md-6">

                            <input id="appointmentTimeBusiness" type="time" placeholder="Appointment time..." class="form-control @error('appointmentTimeBusiness') is-invalid @enderror" name="appointmentTimeBusiness"  autocomplete="appointmentTimeBusiness">

                            @error('appointmentTimeBusiness')
                            <span class="invalid-feedback" role="alert">
                            <strong>{{ $message }}</strong>
                           </span>
                            @enderror
                            </div>
                        </div>

                        

                        <div class="form-group row">
                            <label for="phoneBusiness" class="col-md-4 col-form-label text-md-right">{{ __('Phone') }}</label>

                            <div class="col-md-6">
                                <input id="phoneBusiness" type="tel" placeholder="Phone..." class="form-control @error('phoneBusiness') is-invalid @enderror" name="phoneBusiness"  autocomplete="phoneBusiness">

                                @error('phoneBusiness')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="emailBusiness" class="col-md-4 col-form-label text-md-right">{{ __('Email') }}</label>

                            <div class="col-md-6">
                                <input id="emailBusiness" type="email" placeholder="Email..." class="form-control @error('emailBusiness') is-invalid @enderror" name="emailBusiness"  autocomplete="emailBusiness">

                                @error('emailBusiness')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <h3>Address</h3>

                        <br>

                        <div class="form-group row">
                            <label for="streetBusiness" class="col-md-4 col-form-label text-md-right">{{ __('Street') }}</label>

                            <div class="col-md-6">
                                <input id="streetBusiness" type="text" placeholder="Street..." class="form-control @error('streetBusiness') is-invalid @enderror" name="streetBusiness"  autocomplete="streetBusiness">

                                @error('streetBusiness')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="houseNumberBusiness" class="col-md-4 col-form-label text-md-right">{{ __('House number') }}</label>

                            <div class="col-md-6">
                                <input id="houseNumberBusiness" type="number" placeholder="House Number..." class="form-control @error('houseNumberBusiness') is-invalid @enderror" name="houseNumberBusiness"  autocomplete="houseNumberBusiness">

                                @error('houseNumberBusiness')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="cityBusiness" class="col-md-4 col-form-label text-md-right">{{ __('City') }}</label>

                            <div class="col-md-6">
                                <input id="cityBusiness" type="text"  placeholder="City..." class="form-control @error('cityBusiness') is-invalid @enderror" name="cityBusiness"  autocomplete="cityBusiness">

                                @error('cityBusiness')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="postalcodeBusiness" class="col-md-4 col-form-label text-md-right">{{ __('Postalcode') }}</label>

                            <div class="col-md-6">
                                <input id="postalcodeBusiness" type="number" placeholder="Postalcode..." class="form-control @error('postalcodeBusiness') is-invalid @enderror" name="postalcodeBusiness"  autocomplete="postalcodeBusiness">

                                @error('postalcodeBusiness')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="countryBusiness" class="col-md-4 col-form-label text-md-right">{{ __('Country') }}</label>

                            <div class="col-md-6">
                                <select id="countryBusiness" type="text"  class="form-control @error('countryBusiness') is-invalid @enderror" name="countryBusiness"  autocomplete="countryBusiness">

                                <option value="Belgium">Belgium</option>
                                </select>

                                @error('countryBusiness')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <br>


                        


                        <br>
                        <br>
                    
                        
                                <button type="submit" class="btn btn-dark addBusinessBtn">
                                    {{ __('Add Business') }}
                                </button>
                        
                            
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection

</body>
</html>