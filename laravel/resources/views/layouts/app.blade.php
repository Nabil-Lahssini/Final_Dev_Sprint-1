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
    <script src="fullcalendar/list/main.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>

    <!-- Fonts -->
    <link rel="dns-prefetch" href="//fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet">

    <!-- Styles -->
    <link href="{{ asset('css/app.css') }}" rel="stylesheet">
    <link rel="stylesheet" href="fullcalendar/core/main.css">
    <link rel="stylesheet" href="fullcalendar/daygrid/main.css">
    <link rel="stylesheet" href="fullcalendar/timegrid/main.css">
    <link rel="stylesheet" href="fullcalendar/list/main.css">
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


        <main>
            @include('layouts.partials.nav')
            @yield('content')
            @include('layouts.partials.footer')
        </main>



    </div>
</body>

</html>
