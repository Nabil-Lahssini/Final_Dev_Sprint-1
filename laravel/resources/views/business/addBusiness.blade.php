<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <style>
        .registerBtnAndLink{
            float: right;
        }

        #AlreadyRegistred{
            margin-right: 30px;
           
        }

        .registerBtn{
            margin-right: 20px;
        }

        #gender:hover {
            cursor: pointer;
        }

        .registerBox h3{
            margin-left: 40px;
        }


    </style>
</head>
<body>
    


@extends('layouts.app')

@section('content')


<div class="container py-5 registerBox">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                

                <div class="card-body">
                    <form method="POST" action="{{ route('register') }}">
                        @csrf

                        <br>

                        <h3>Account Information</h3>

                        <br>

                        <div class="form-group row">
                            <label for="nameBusiness" class="col-md-4 col-form-label text-md-right">{{ __('Name') }}</label>

                            <div class="col-md-6">
                                <input id="nameBusiness" type="text" class="form-control @error('nameBusiness') is-invalid @enderror" name="nameBusiness" required autocomplete="nameBusiness">

                                @error('nameBusiness')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="type" class="col-md-4 col-form-label text-md-right">{{ __('Gender') }}</label>

                            <div class="col-md-6">

                            <select name="type"  id="type" class="form-control @error('type') is-invalid @enderror"  required autocomplete="type">

                            <option value="Kapper">Kapper</option>
                            <option value="Esthetique">Esthetique</option>

                            </select>
                               

                                @error('type')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        

                        <div class="form-group row">
                            <label for="phone" class="col-md-4 col-form-label text-md-right">{{ __('Phone') }}</label>

                            <div class="col-md-6">
                                <input id="phone" type="tel" class="form-control @error('phone') is-invalid @enderror" name="phone" required autocomplete="phone">

                                @error('phone')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <h3>Addres</h3>

                        <br>

                        <div class="form-group row">
                            <label for="street" class="col-md-4 col-form-label text-md-right">{{ __('Street') }}</label>

                            <div class="col-md-6">
                                <input id="street" type="text" class="form-control @error('street') is-invalid @enderror" name="street" required autocomplete="street">

                                @error('street')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="houseNumber" class="col-md-4 col-form-label text-md-right">{{ __('House number') }}</label>

                            <div class="col-md-6">
                                <input id="houseNumber" type="number" class="form-control @error('street') is-invalid @enderror" name="houseNumber" required autocomplete="houseNumber">

                                @error('houseNumber')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="city" class="col-md-4 col-form-label text-md-right">{{ __('City') }}</label>

                            <div class="col-md-6">
                                <input id="city" type="text" class="form-control @error('city') is-invalid @enderror" name="city" required autocomplete="city">

                                @error('city')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="postalcode" class="col-md-4 col-form-label text-md-right">{{ __('Postalcode') }}</label>

                            <div class="col-md-6">
                                <input id="postalcode" type="number" class="form-control @error('postalcode') is-invalid @enderror" name="postalcode" required autocomplete="postalcode">

                                @error('postalcode')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="country" class="col-md-4 col-form-label text-md-right">{{ __('Country') }}</label>

                            <div class="col-md-6">
                                <input id="country" type="text" class="form-control @error('country') is-invalid @enderror" name="country" required autocomplete="country">

                                @error('country')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <br>


                        


                        <br>
                        <br>

                        
                        <div class="registerBtnAndLink">


                        <a href="{{ route('login') }}" id="AlreadyRegistred">Already Registred?</a>
                        
                                <button type="submit" class="btn btn-dark registerBtn">
                                    {{ __('Register') }}
                                </button>
                        </div>
                            
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection

</body>
</html>