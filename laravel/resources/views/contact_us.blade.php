@extends('layouts.app')
@section('content')


<section class="jumbotron text-center" style="margin-bottom: 16px;">
    <div class="container">
        <h1 class="jumbotron-heading">CONTACT US</h1>
        <p class="lead text-muted mb-0">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua</p>
    </div>
</section>
<div class="container" >
    <div class="row">
        <div class="col">
            <nav aria-label="breadcrumb">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item"><a href="{{ url('/') }}">Home</a></li>
                    <li class="breadcrumb-item active" aria-current="page">Contact</li>
                </ol>
            </nav>
        </div>
    </div>
</div>
<div class="container" style="padding-bottom: 107px; padding-top: 0px;">
    <div class="row">
        <div class="col">
            <div class="card">
                <div class="card-header bg-secondary text-white"><i class="fa fa-envelope"></i> Contact us.
                </div>
                <div class="card-body" style="padding-top: 16px;">
                    <form>
                        <div class="form-group">
                            <label for="name">Name</label>
                            <input type="text" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Enter name" required>
                        </div>
                        <div class="form-group">
                            <label for="email">Email address</label>
                            <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Enter email" required>
                            <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
                        </div>
                        <div class="form-group">
                            <label for="message">Message</label>
                            <textarea class="form-control" id="message" rows="6" required></textarea>
                        </div>
                        <div class="mx-auto">
                            
                            <button type="submit" class="btn btn-secondary text-right">Submit</button></div>

                    </form>
                </div>
            </div>
        </div>
        <div class="col-12 col-sm-4">
            <div class="card bg-light mb-3">
                <div class="card-header bg-secondary text-white text-uppercase"><i class="fa fa-home"></i> Address</div>
                <div class="card-body" style="padding-top: 16px;">
                    <p>Quai de l'Industrie 170</p>
                    <p>1000 Bruxelles</p>
                    <p>Belgique</p>
                    <p>Email : plannify@contact.com</p>
                    <p>Tel. +32 04 56 11 51 84</p>

                </div>

            </div>
        </div>
    </div>
</div>

@endsection