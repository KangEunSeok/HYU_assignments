import React, { Component } from 'react';
import moment from 'moment';
import { Link } from 'react-router-dom';
import './EventList.css'

const axios = require('axios');

class EventList extends Component {
  state={
  }
  componentWillMount(){
    this._getPartEventList();
    this._getVolEventList();
  }

  _getPartEventList = async () => {
    const PartEvents = await this.getPartEventApi()
    this.setState({
      PartEvents
    })
  }

  getPartEventApi = () => {
    var _id = localStorage.getItem("userId")
    return axios.get('http://54.180.25.155:8020/users/'+_id+'/participant')
    .then(response => response.data)  
    .catch(err => console.log(err))
  }

  _getVolEventList = async () => {
    const VolEvents = await this.getVolEventApi()
    this.setState({
      VolEvents
    })
  }

  getVolEventApi = () => {
    var _id = localStorage.getItem("userId")
    return axios.get('http://54.180.25.155:8020/users/'+_id+'/volunteer')
    .then(response => response.data)  
    .catch(err => console.log(err))
  }


  _setLocalStorage = (_eid) => {
    localStorage.setItem('eid',_eid)
  }

   _delPartEvent = async (_eid) => {
    let data = new FormData();
    let userId = localStorage.getItem("userId")
    data.append('uid',userId)
    data.append('eid',_eid)
    return axios.post('http://54.180.25.155:8020/delete/participant', data)
    .then(function (response) {
      console.log(response);
      alert("해당 행사신청이 취소 되었습니다.")
      window.location.reload();
    })  
    .catch(err => console.log(err))
  }

  _delVolEvent = async (_eid) => {
    let data = new FormData();
    let userId = localStorage.getItem("userId")
    data.append('eid',_eid)
    data.append('uid',userId)
    return axios.post('http://54.180.25.155:8020/delete/volunteer', data)
    .then(function (response) {
      console.log(response);
      alert("해당 행사신청이 취소 되었습니다.")
      window.location.reload();
    })  
    .catch(err => console.log(err))
  }

  render(){
    return(
      <div>
      <div className="card">
        <div className="header text-center">
          <h4 className="title">참가자 신청 행사 목록</h4>
          <br />
        </div>
        <div className="content table-responsive table-full-width">
          <table className="table table-bigboy">
            <thead>
              <tr>
                <th className="text-center"></th>
                <th>행사 장소 </th>
                <th>행사 내용</th>
                <th>행사 날짜</th>
              </tr>
            </thead>
            <tbody>
              {this.state.PartEvents && this.state.PartEvents.map((event) => (
                <tr>
                  <td>
                    <div className="image-size">
                      <img src={event.eventImage} />
                    </div>
                  </td>
                  <td className="td-name">
                    {event.place}
                  </td>
                  <td>
                    {event.intention}
                  </td>
                  <td>
                    {moment(event.event_date).format('YYYY-MM-DD')}
                  </td>
                  <td className="td-actions">
                    <Link to="/ApplyedPart">
                      <button className="btn btn-fill btn-rectangle btn-wd" onClick={this._setLocalStorage.bind(null,event.eid)}>수정</button>
                    </Link>
                    <tr></tr>
                      <button className="btn btn-rectangle btn-wd" onClick={this._delPartEvent.bind(null,event.eid)}>삭제</button>
                  </td>
                </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
    <div className="card">
        <div className="header text-center">
          <h4 className="title">봉사자 신청 행사 목록</h4>
          <br />
        </div>
        <div className="content table-responsive table-full-width">
          <table className="table table-bigboy">
            <thead>
              <tr>
                <th className="text-center"></th>
                <th>행사 장소 </th>
                <th>행사 내용</th>
                <th>행사 날짜</th>
              </tr>
            </thead>
            <tbody>
              {this.state.VolEvents && this.state.VolEvents.map((event) => (
                <tr>
                  <td>
                    <div className="image-size">
                      <img src={event.eventImage} />
                    </div>
                  </td>
                  <td className="td-name">
                    {event.place}
                  </td>
                  <td>
                    {event.intention}
                  </td>
                  <td>
                    {moment(event.event_date).format('YYYY-MM-DD')}
                  </td>
                  <td className="td-actions">
                    <Link to="/ApplyedVol">
                      <button className="btn btn-fill btn-rectangle btn-wd" onClick={this._setLocalStorage.bind(null,event.eid)}>수정</button>
                    </Link>
                    <tr></tr>
                      <button className="btn btn-rectangle btn-wd" onClick={this._delVolEvent.bind(null,event.eid)}>삭제</button>
                  </td>
                </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
    </div>
    )
  }
}


export default EventList;