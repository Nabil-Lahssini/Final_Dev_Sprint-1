<!doctype html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- CSRF Token -->
    <meta name="csrf-token" content="{{ csrf_token() }}">

    <title>{{ config('app.name', 'Laravel') }}</title>

    <!-- Scripts -->
    <script src="fullcalendar/core/main.js"></script>
    <script src="fullcalendar/daygrid/main.js"></script>
    <script src="fullcalendar/timegrid/main.js"></script>
    <script src="{{ asset('js/app.js') }}" defer></script>
<<<<<<< HEAD
    <script src="fullcalendar/list/main.js"></script>
=======
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
<<<<<<< HEAD
    <script src="{{ asset('js/Dashboard.js') }}"></script>
=======
>>>>>>> f47ac079494430676bb8e78664f481befef59a8f
>>>>>>> 5aba4a99ebe41f1875991b86d859df4231032eee

    <!-- Fonts -->
    <link rel="dns-prefetch" href="//fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet">

    <!-- Styles -->
    <link href="{{ asset('css/app.css') }}" rel="stylesheet">
<<<<<<< HEAD
    <link href="{{ asset('css/Dashboard.css') }}" rel="stylesheet">
=======
    <link rel="stylesheet" href="fullcalendar/core/main.css">
    <link rel="stylesheet" href="fullcalendar/daygrid/main.css">
    <link rel="stylesheet" href="fullcalendar/timegrid/main.css">
    <link rel="stylesheet" href="fullcalendar/list/main.css">
>>>>>>> 5aba4a99ebe41f1875991b86d859df4231032eee
</head>

<body>
    <style>
        html,
        body {
            margin: 0;
            padding: 0;
            height: 100%;
        }

        /* img {
            background-size: 100em;
            /* background: no-repeat center 2em; */
        } */
    </style>
    <div id="app">
<<<<<<< HEAD
        <nav class="navbar navbar-expand-md navbar-light bg-white shadow-sm">
            <div class="container">
                <a class="navbar-brand" href="{{ url('/') }}">
                    {{ config('app.name', 'Laravel') }}
                </a>
                <button class="navbar-toggler" type="button" data-toggle="collapse"
                    data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                    aria-label="{{ __('Toggle navigation') }}">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <!-- Left Side Of Navbar -->
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item">
                            <a class="nav-link" href="{{ route('apointment.index') }}">appointment</a>
                        </li>
                    </ul>

                    <!-- Right Side Of Navbar -->
                    <ul class="navbar-nav ml-auto">
                        <!-- Authentication Links -->
                        @guest
                        @if (Route::has('login'))
                        <li class="nav-item">
                            <a class="nav-link" href="{{ route('login') }}">{{ __('Login') }}</a>
                        </li>
                        @endif

                        @if (Route::has('register'))
                        <li class="nav-item">
                            <a class="nav-link" href="{{ route('register') }}">{{ __('Register') }}</a>
                        </li>
                        @endif
                        @else
                        <li class="nav-item dropdown">
                            <a id="navbarDropdown" class="nav-link dropdown-toggle" href="#" role="button"
                                data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" v-pre>
                                {{ Auth::user()->name }}
                            </a>

                            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">
                                <a class="dropdown-item" href="{{ route('logout') }}" onclick="event.preventDefault();
                                                     document.getElementById('logout-form').submit();">
                                    {{ __('Logout') }}
                                </a>

                                <form id="logout-form" action="{{ route('logout') }}" method="POST" class="d-none">
                                    @csrf
                                </form>
                            </div>
                        </li>
                        @endguest
                    </ul>
                </div>
            </div>
        </nav>
=======


        <main>
            @include('layouts.partials.nav')
            @yield('content')
            @include('layouts.partials.footer')
        </main>


>>>>>>> f47ac079494430676bb8e78664f481befef59a8f

    </div>
</body>

<<<<<<< HEAD
</html>
=======
</html>
>>>>>>> f47ac079494430676bb8e78664f481befef59a8f
