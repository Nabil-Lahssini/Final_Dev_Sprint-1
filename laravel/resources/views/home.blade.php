@extends('layouts.app')

@section('content')

    <div class="container">
    <div id="calendar">

    </div>
    </div>


@endsection
<script>

    window.onload=() =>{
        let elementCalender = document.getElementById('calendar');
        //We make an instance of the calendar
        let calendar= new FullCalendar.Calendar(elementCalender,{
            //we call the compenents
            plugins: ['dayGrid']
        })
        calendar.render();
    }
</script>