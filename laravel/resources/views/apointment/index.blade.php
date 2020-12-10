@extends('layouts.app')

@section('content')

    <div class="container">
    <div id="calendar" class="py-5">

    </div>
    </div>


@endsection
<script>
    //Test without api
    let event = [{
        "title": "Programming project - sessie ?",
        "start": "2020-12-10 10:10:00",
        "end": "2020-12-10 11:00:00"
    },
    {
        "title": "project final  - sessie ?",
        "start": "2020-12-11 10:10:00",
        "end": "2020-12-11 11:30:00"
    }
];

    window.onload=() =>{
        let elementCalender = document.getElementById('calendar');
        //We make an instance of the calendar
        let calendar= new FullCalendar.Calendar(elementCalender,{
            //we call the compenents
            plugins: ['dayGrid','timeGrid','list'],
            defaultView:'timeGridWeek',
            locale:'en',
        
            header:{
                //previous and next week
                left:'prev ,next today',
                //title=dateTime
                center:'title',
                
                right:'dayGridMonth,timeGridWeek,list'
            },
            buttonText:{
                today: 'Today',
                month:'Month',
                week:'Week',
                list:'List'
            },
            events:event
        })
        calendar.render();
    }
</script>