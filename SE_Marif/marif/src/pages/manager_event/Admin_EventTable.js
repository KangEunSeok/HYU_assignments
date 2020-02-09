import React, { Component } from 'react';
import moment from 'moment';
import { Link } from 'react-router-dom';
import './Admin_EventTable.css'

const axios = require('axios');

class Admin_EventTable extends Component {
  state={
  }
  componentWillMount(){
    this._getEventList();
    this._getPartVolList();
  }

  _getEventList = async () => {
    const Event = await this.getEventApi()
    this.setState({
      Event
    })
  }

  getEventApi = () => {
    var _eid = localStorage.getItem('admin_eid')
    console.log(_eid)
    return axios.get('http://54.180.25.155:8020/event'+'/'+_eid)
    .then(response => response.data)  
    .catch(err => console.log(err))
  }

  _getPartVolList = async () => {
    const parts = await this._getPartApi()
    const vols = await this._getVolApi()
    console.log(parts)
    console.log(vols)
    this.setState({
      parts
    })
    this.setState({
      vols
    })
  }

  _getPartApi = () => {
    var _eid = localStorage.getItem('admin_eid')
    console.log(_eid)
    return axios.get('http://54.180.25.155:8020/admin/' + _eid +'/participants')
    .then(response => response.data)  
    .catch(err => console.log(err))
  }
  _getVolApi = () => {
    var _eid = localStorage.getItem('admin_eid')
    console.log(_eid)
    return axios.get('http://54.180.25.155:8020/admin/' + _eid +'/volunteers')
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
              {this.state.Event && this.state.Event.map((event) => (
              <thead> 
                <td>
                  <div className="event-image-size">
                    <img src={event.eventImage} />
                  </div>
                  <br/> <br/>
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
                </td>
              </thead>
              ))}
              <tbody>
                <tr>
                <h4 className="title">참가자 리스트 </h4>
                <br />
                </tr>
                <br/>
              {!(this.state.parts) ? "참가자가 없습니다." : "" }
                <br/>
              {this.state.parts && this.state.parts.map((part) => (
                <td className="td-name">
                  <tr> 이름 : {part.pname}, 나이 : {part.age}</tr>
                  <tr> 핸드폰 : {part.phoneNumber} </tr>
                  <tr> 지원경로 : {part.joinPath} </tr>
                  <tr> 동반자 수 : {part.partner} </tr>
                  <tr> 반려견 양육 유무 : {part.pet_experience === false ? "없음" : "있음"} </tr>
                  <tr> 반려견 양육 기간 : {part.pet_period === null ? "없음" : part.pet_period} </tr>
                  <br />
                </td>
              ))}
                <br/>
                <tr>
                <h4 className="title">봉사자 리스트 </h4>
                <br />
                </tr>
                <br/>
              {!(this.state.vols) ? "봉사자가 없습니다." : "" }
                
              {this.state.vols && this.state.vols.map((vol) => (
                <td className="td-name">
                  <tr> 이름 : {vol.pname}, 나이 : {vol.age}</tr>
                  <tr> 핸드폰 : {vol.phoneNumber} </tr>
                  <tr> 지원경로 : {vol.joinPath} </tr>
                  <tr> 반려견 양육 유무 : {vol.pet_experience === false ? "없음" : "있음"} </tr>
                  <tr> 반려견 양육 기간 : {vol.pet_period === null ? "없음" : vol.pet_period} </tr>
                  <br />
                </td>
              ))}

                <tr>
                  <br/>
                  <Link to="/manager_ManageEvent">
                    <button className="btn btn-fill btn-rectangle btn-wd" >목록으로 돌아가기</button>
                  </Link>
                </tr>   
              </tbody>
        </table>
      </div>
      </div>
    )
  }
}


export default Admin_EventTable;