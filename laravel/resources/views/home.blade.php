@extends('layouts.app')
@section('content')
<section class="jumbotron text-center" style="padding-top: 20px; margin-bottom:0px; ">
    <div class="container">
        <h1 class="jumbotron-heading" >Welcome</h1>
        <!-- <img src="{{ asset('images/planify.png') }}" alt="main-page-logo"> -->
        <p class="lead text-muted">"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>

        <div class="input-group mb-4 border rounded-pill p-1">
            <input type="search" placeholder="What're you searching for?" aria-describedby="button-addon3" class="form-control bg-none border-0">

        </div>
        <div style="width: 930px; height:620px;" class="container">

            <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
                <ol class="carousel-indicators">
                    <li data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active"></li>
                    <li data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1"></li>
                    <li data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2"></li>
                </ol>
                <div class="carousel-inner">
                    <div class="carousel-item active ">
                        <img src="{{ asset('images/Carousel1.png') }}" style="display: block" class="d-block w-100" alt="...">
                        <div class="carousel-caption d-none d-md-block">
                            <h5>First slide label</h5>
                            <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
                        </div>
                    </div>
                    <div class="carousel-item ">
                        <img src="{{ asset('images/Carousel2.png') }}" class="d-block w-100" alt="...">
                        <div class="carousel-caption d-none d-md-block">
                            <h5>Second slide label</h5>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img src="{{ asset('images/Piece-carousel3.png') }}" class="d-block w-100" alt="...">
                        <div class="carousel-caption d-none d-md-block">
                            <h5>Third slide label</h5>
                            <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                        </div>
                    </div>
                </div>
                <a class="carousel-control-prev" href="#carouselExampleCaptions" role="button" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </a>
                <a class="carousel-control-next" href="#carouselExampleCaptions" role="button" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </a>
            </div>
        </div>


    </div>
</section>

<!-- <section class="jumbotron text-center">
    <div class="container">
        <h1 class="jumbotron-heading">About us </h1>
        <p class="lead text-muted">"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                Ut enim ad minim veniam, excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>
        <p>
            <a href="{{ url('/login') }}" class="btn btn-primary">Login</a>
            <a href="{{ url('/register') }}" class="btn btn-secondary">Register</a>
        </p>
    </div>
</section> -->


@endsection