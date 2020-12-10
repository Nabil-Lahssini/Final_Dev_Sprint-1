@extends('layouts.app')

@section('content')
<!--DateTime-local not supported in firefox and safari  -->
<div class="container py-5">
    <form action="/profile" method="post">
    @csrf
    <div class="form-group">
            <label class="form-control-label" >Start</label>
            <input type="datetime-local" name="start"  class="form-control form-control-alternative @error('start') is-invalid @enderror" placeholder="Start">
            @error('start')
            <div class="alert  alert-danger"> {{$errors->first('start')}}</div>
            @enderror
        </div>
        <div class="form-group">
            <label class="form-control-label" >End</label>
            <input type="datetime-local" name="end" class="form-control form-control-alternative @error('start') is-invalid @enderror" placeholder="End time">
            @error('end')
            <div class="alert  alert-danger"> {{$errors->first('end')}}</div>
            @enderror
        </div>
        <div class="form-group">
            <label class="form-control-label" >Name</label>
            <input type="text"  name="title" class="form-control form-control-alternative @error('name') is-invalid @enderror" placeholder="Your name">
            @error('name')
            <div class="alert  alert-danger">{{$errors->first('name')}} </div>
            @enderror
        </div>
        <div class="form-group">
            <label class="form-control-label" >Description</label>
            <input  type="text"  name="description" class="form-control form-control-alternative @error('description') is-invalid @enderror" placeholder="Description of your visit">
            @error('description')
            <div class="alert  alert-danger"> {{$errors->first('description')}}</div>
            @enderror
        </div>
        <button type="submit" class="btn btn-secondary">Submit</button>
    </form>

</div>
@endsection
