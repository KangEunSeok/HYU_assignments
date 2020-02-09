import React, { Component } from 'react';
import moment from 'moment';
import { Link } from 'react-router-dom';
import './EventTable.css'

const axios = require('axios');

class EventTable extends Component {
  state={
  }
  componentWillMount(){
    this._getEventList();
  }

  _getEventList = async () => {
    const Event = await this.getEventApi()
    this.setState({
      Event
    })
  }

  getEventApi = () => {
    var _eid = localStorage.getItem('eid')
    return axios.get('http://54.180.25.155:8020/event'+'/'+_eid)
    .then(response => response.data)  
    .catch(err => console.log(err))
  }

  render(){
    return(
      <div className="card">
        <div className="header text-center">
          <h4 className="title">마리프 행사 소개 </h4>
          <br />
        </div>
        <div className="content table-responsive table-full-width">
          <table className="table table-bigboy">
            <thead>
            </thead>
              {this.state.Event && this.state.Event.map((event) => (
              <tbody> 
                <td>
                  <div className="event-image-size">
                    <img src={event.eventImage} />
                  </div>
                </td>
                <td className="td-name">
                  <tr>행사 소개 내용</tr>
                  <tr>행사 명 : 마리프 - 유기견 산책행사</tr>
                  <tr>행사 주최 : {event.host}</tr>
                  <tr>행사 의도 : {event.intention}</tr>
                  <tr>행사 내용 : {event.event_info ? event.event_info : "no info"}</tr> 
                  <tr>행사 장소 : {event.place}</tr>
                  <tr>행사 일시 : {event.event_date.year + "/" + event.event_date.monthValue + "/" + event.event_date.dayOfMonth + "   " + event.event_date.hour + ":" + event.event_date.minute}</tr>
                  <tr> 신청 가능한 참가자 수 : {event.max_participant - event.current_participant} </tr>
                  <tr> 신청 가능한 봉사자 수 : {event.max_volunteer}</tr>
                  <br />
                  <tr>
                    <Link to="/ApplyPart">
                      <button className="btn btn-fill btn-rectangle btn-wd"> 참가자 신청하기</button>
                    </Link>
                    <Link to="/ApplyVol">
                      <button className="btn btn-fill btn-rectangle btn-wd">봉사자 신청하기</button>
                    </Link>
                  </tr>
                  <tr>
                    <Link to="/test">
                      <button className="btn btn-fill btn-rectangle btn-wd" >목록으로 돌아가기</button>
                    </Link>
                  </tr>
                </td>
              </tbody>
              ))}   
        </table>
      </div>
      </div>
    )
  }
}


export default EventTable;