import React, {Component} from 'react';
import ReactDOM from 'react';
import './UploadEvent.css'
import { Field, reduxForm } from 'redux-form';
import { Link } from 'react-router-dom';
import renderField from 'components/FormInputs/renderField';
import axios from 'axios';
import Calendar from 'react-calendar';
import Alert from 'sweetalert-react';

class ImageUpload extends Component {
  constructor(props) {
    super(props);
    this.handleHost = this.handleHost.bind(this);
    this.handleIntention = this.handleIntention.bind(this);
    this.handleMax_participant = this.handleMax_participant.bind(this);
    this.handleMax_volunteer = this.handleMax_volunteer.bind(this);
    this.handlePlace = this.handlePlace.bind(this);
    this.handleInfo = this.handleInfo.bind(this);
    this.state = {
      file: '',
      imagePreviewUrl: '',
      Event_contents:'',
      host:'',
      intention:'',
      max_participant:0,
      max_volunteer:0,
      place:'',
      eventInfo:'',
      date: new Date(),
      test: true,
      testCancel: true
    };
  }
  testState ={}
  _onChange = date => this.setState({date})

  handleHost(e){
    this.setState({host:e.target.value})
  }
  handleIntention(e){
    this.setState({intention:e.target.value}) 
  }
  handleMax_participant(e){
    this.setState({max_participant:e.target.value}) 
  }
  handleMax_volunteer(e){
    this.setState({max_volunteer:e.target.value}) 
  }
  handlePlace(e){
    this.setState({place:e.target.value}) 
  }
  handleInfo(e){
    this.setState({eventInfo:e.target.value}) 
  }
  

  _handleSubmit(e) {
    e.preventDefault();
    // TODO: do something with -> this.state.file
    console.log('handle uploading-', this.state.file);

      let data = new FormData();
     data.append('host',this.state.host);
     data.append('intention', this.state.intention);
     data.append('max_participant',this.state.max_participant);
     data.append('max_volunteer',this.state.max_volunteer);
     data.append('place',this.state.place);
     data.append('file',this.state.file);
     data.append('event_date',this.state.date.toISOString().substring(0,10));
     data.append('event_info',this.state.eventInfo); 
      data.forEach((value,key) => {
      console.log(key+" "+value)
    });    
    axios.post('http://54.180.25.155:8020/admin/event/register', data)
      .then(function (response) {
           console.log(response);
            window.location.reload();
      }).catch(function (error) {
           console.log(error);
      });

    /* data console */
   


  }

  
  _handleImageChange(e) {
    e.preventDefault();

    let reader = new FileReader();
    let file = e.target.files[0];

    reader.onloadend = () => {
      this.setState({
        file: file,
        imagePreviewUrl: reader.result
      });
    }
    if(file != null)
    reader.readAsDataURL(file)
  }

  render() {
    let {imagePreviewUrl} = this.state;
    let $imagePreview = null;
    if (imagePreviewUrl) {
      $imagePreview = (<img src={imagePreviewUrl} />);
    } else {
      $imagePreview = (<div className="previewText">Please select an Image for Preview</div>);
    }

    return (
    <div className="card">
    <div className = "row">
      <div className="col-md-6">
      <div className="previewComponent">
      <div className="imgPreview">
          {$imagePreview}
        </div>
        <form onSubmit={(e)=>this._handleSubmit(e)}>
          <input className="fileInput" 
            type="file" 
            onChange={(e)=>this._handleImageChange(e)} />
          
        </form>
        </div>
      </div>
      <div className = "col-md-6">
           <form className="form-horizontal">
            <div className="content">
            <div className="form-group">
                <label className="col-sm-3 control-label"></label>
                <div className="col-sm-9">
                 <input className="" placeholder="행사 내용 입력" onChange={this.handleInfo}/> 
                </div>
              </div>
              <div className="form-group">
                <label className="col-sm-3 control-label">주 최</label>
                <div className="col-sm-9">
                 <input className="" onChange={this.handleHost}/> 
                </div>
              </div>

              <div className="form-group">
                <label className="col-sm-3 control-label">취 지</label>
                <div className="col-sm-9">
                  <input className="" onChange={this.handleIntention}/> 
                </div>
              </div>

              <div className="form-group">
                <label className="col-sm-3 control-label">참가자 수</label>
                <div className="col-sm-9">
                   <input className="" onChange={this.handleMax_participant}/> 
                </div>
              </div>

              <div className="form-group">
                <label className="col-sm-3 control-label">봉사자 수</label>
                <div className="col-sm-9">
                   <input className="" onChange={this.handleMax_volunteer}/> 
                </div>
              </div>

              <div className="form-group">
                <label className="col-sm-3 control-label">장 소</label>
                <div className="col-sm-9">
                   <input className="" onChange={this.handlePlace}/> 
                </div>
              </div>

              <div className="form-group">
                <label className="col-sm-3 control-label">날짜</label>
                <div className="col-sm-9">
                   <Calendar onChange={this._onChange} value={this.state.date}/> 
                </div>
              </div>
            </div>
            <div className="footer text-center">
              <Link to="./manager_ManageEvent">
              <button type="submit" className="btn btn-info btn-fill" onClick={(e)=>this._handleSubmit(e)}>Submit</button>
              </Link>
            </div>
           
          </form>
      </div>
      
    </div>
    </div>

    )
  }
}
export default ImageUpload;