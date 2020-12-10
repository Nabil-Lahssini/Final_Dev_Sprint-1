@extends('layouts.app')
@section('content')

<script>
    //Test without api
    let event = [{
            "id": "1",
            "start": "2020-12-18 13:59:00",
            "end": "2020-12-19 14:59:00",
            "title": "omer",
            "description": "baard",
            "created_at": "2020-12-10 11:58:17",
            "updated_at": "2020-12-10 11:58:17"
        },
        {
            "id": "2",
            "start": "2020-12-11 15:35:00",
            "end": "2020-12-11 16:37:00",
            "title": "omer can ozdmir",
            "description": "haar",
            "created_at": "2020-12-10 12:35:13",
            "updated_at": "2020-12-10 12:35:13"
        }
    ];

    window.onload = () => {
        document.getElementById('LondonButton').click();
        let elementCalender = document.getElementById('calendar');
        //We make an instance of the calendar
        let calendar = new FullCalendar.Calendar(elementCalender, {
            //we call the compenents
            plugins: ['dayGrid', 'timeGrid', 'list'],
            initialView: 'dayGridMonth',
            locale: 'en',

            header: {
                //previous and next week
                left: 'prev ,next today',
                //title=dateTime
                center: 'title',

                right: 'dayGridMonth,timeGridWeek,list'
            },
            buttonText: {
                today: 'Today',
                month: 'Month',
                week: 'Week',
                list: 'List'
            },
            events: event,
            nowIndicator: true
        })
        calendar.render();
    }

</script>

<div class="tab container">
    <button class="tablinks" id="LondonButton" onclick="openCity(event, 'London')">Account</button>
    <button class="tablinks" onclick="openCity(event, 'Paris')">Calendar</button>
    <button class="tablinks" onclick="openCity(event, 'Tokyo')">Logout</button>
</div>

<!-- Tab content -->
<!-- Profile tab -->
<div id="London" class="tabcontent container">

    <div class="card-body .py-nopadding  container" style='padding-top: 0px'>
        <p style="padding-top: 16px; font-size:2em;">Account information</p>
        <hr class=" ">
        <form>

            <h6 class="heading-small text-muted mb-4">User information</h6>
            <div class="pl-lg-4">

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-group focused">
                            <label class="form-control-label" for="input-username">First name</label>
                            <input type="text" id="input-username" class="form-control form-control-alternative"
                                placeholder="First name" value="">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-group">
                            <label class="form-control-label" for="input-email">Last name</label>
                            <input type="email" id="input-email" class="form-control form-control-alternative"
                                placeholder="Last name">
                            <input type="text" id="" class="form-control form-control-alternative"
                                placeholder="Last name">
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-6">
                        <label class="form-control-label" for="input-email">Gender</label>
                        <select name="gender" id="gender" class="form-control @error('gender') is-invalid @enderror"
                            required autocomplete="gender">
                            <option value="Men">---</option>
                            <option value="Men">Men</option>
                            <option value="Women">Women</option>
                            <option value="Women">Other</option>
                        </select>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-group focused">

                            <label class="form-control-label" for="input-last-name">¨Phone</label>
                            <input type="text" id="input-last-name" class="form-control form-control-alternative"
                                placeholder="Phone" value="">
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-group focused">
                            <label class="form-control-label" for="input-first-name">Email</label>
                            <input type="text" id="input-first-name" class="form-control form-control-alternative"
                                placeholder="email@example.com" value="">
                            <input type="e-mail" id="input-email" class="form-control form-control-alternative"
                                placeholder="email@example.com" value="">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-group focused">
                            <label class="form-control-label" for="input-last-name">Birthdate</label>
                            <input id="birthdate" type="date"
                                class="form-control @error('birthdate') is-invalid @enderror" name="birthdate" required
                                autocomplete="birthdate">
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-group focused">
                            <label class="form-control-label" for="input-first-name">Password</label>
                            <input id="password" type="password"
                                class="form-control @error('password') is-invalid @enderror" name="password" required
                                autocomplete="new-password" placeholder="Must have at least 8 characters">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-group focused">
                            <label class="form-control-label" for="input-last-name">Confirm password</label>
                            <input id="password-confirm" type="password" class="form-control"
                                name="password_confirmation" required autocomplete="new-password"
                                placeholder="Must have at least 8 characters">
                        </div>
                    </div>
                </div>
            </div>
            <hr class="my-4">
            <!-- Address -->
            <h6 class="heading-small text-muted mb-4">Business information</h6>
            <div class="pl-lg-4">
                <div class="row">
                    <div class="col-md-12">
                        <div class="form-group focused">
                            <label class="form-control-label" for="input-address">Address</label>
                            <input id="input-address" class="form-control form-control-alternative"
                                placeholder="Home Address" value="Quai de l'Industrie 170" type="text">
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-4">
                        <div class="form-group focused">
                            <label class="form-control-label" for="input-city">City</label>
                            <input type="text" id="input-city" class="form-control form-control-alternative"
                                placeholder="City" value="Brussels">
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="form-group focused">
                            <label class="form-control-label" for="input-country">Country</label>
                            <input type="text" id="input-country" class="form-control form-control-alternative"
                                placeholder="Country" value="Belgium">
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="form-group">
                            <label class="form-control-label" for="input-country">Postal code</label>
                            <input type="number" id="input-postal-code" class="form-control form-control-alternative"
                                placeholder="1070">
                        </div>
                    </div>
                </div>
            </div>
            <!-- <hr class="my-4"> -->
            <br>
            <div class="container">
                <button type="button" class="btn btn-secondary" disabled>Cancel</button>
                <button type="button" class="btn btn-secondary">Submit</button>
            </div>
            <!-- Description -->
            <!-- <h6 class="heading-small text-muted mb-4">About me</h6>
            <div class="pl-lg-4">
                <div class="form-group focused">
                    <label>About Me</label>
                    <textarea rows="4" class="form-control form-control-alternative" placeholder="A few words about you ...">A beautiful Dashboard for Bootstrap 4. It is Free and Open Source.</textarea>
                </div>
            </div> -->
        </form>
    </div>
</div>
</div>
</div>
</div>
</div>
<!-- Profile tab -->
<div id="Paris" class="tabcontent container">
    <div class="card-body .py-nopadding  container" style='padding-top: 0px;'>
        <p style="padding-top: 16px; font-size:2em;">Calendar</p>
        <a href="{{route('create')}}" class="btn btn-primary py-3">Make appointment</a>
        <hr>



        <div class="container">
            <div id="calendar" class="py-5">


            </div>
        </div>

    </div>
</div>

</div>

</div>

<div id="Tokyo" class="tabcontent container">
    <div class="card-body .py-nopadding  container" style='padding-top: 0px'>
        <p style="padding-top: 16px; font-size:2em;">Logout</p>
        <hr>
    </div>
</div>





@endsection
