import React, { Component } from 'react';
import moment from 'moment';
import { Link } from 'react-router-dom';
import './ManagerEventTable.css'

const axios = require('axios');

class ManagerEventTable extends Component {
  state={
  }
  componentWillMount(){
    this._getEventList();
  }

  _getEventList = async () => {
    const Events = await this.getEventApi()
    this.setState({
      Events
    })
  }

  getEventApi = () => {
    return axios.get('http://54.180.25.155:8020/events')
    .then(response => response.data)  
    .catch(err => console.log(err))
  }

  _setLocalStorage = (_eid, path) => {
    localStorage.setItem('admin_eid',_eid)
    localStorage.setItem('imagePath',path)
  }

  _delEvent = async (_eid) => {
    let data = new FormData();
    data.append('eid',_eid)
    return axios.post('http://54.180.25.155:8020/admin/event/delete/', data)
    .then(function (response) {
      console.log(response);
      alert("해당 행사가 삭제 되었습니다.")
      window.location.reload();
    })  
    .catch(err => console.log(err))
  }

  render(){
    return(
      <div className="card">
        <div className="header text-center">
          <h4 className="title">행사 목록</h4>
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
              {this.state.Events && this.state.Events.map((event) => (
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
                    {event.event_date.year + "/" + event.event_date.monthValue + "/" + event.event_date.dayOfMonth + "   " + event.event_date.hour + ":" + event.event_date.minute}
                  </td>
                  <td className="td-modify">
                    <Link to="./manager_ModifyEvent">
                      <button className="btn btn-sm btn-fill btn-rectangle"onClick={this._setLocalStorage.bind(null,event.eid,event.eventImage)} >수정</button>
                    </Link>
                  </td>
                  <td className="td-delete">
                    <button className="btn btn-sm btn-fill btn-rectangle" onClick={this._delEvent.bind(null,event.eid)}>삭제</button>
                  </td>
                  <td className="td-actions">
                    <Link to="/manager_event">
                      <button className="btn btn-fill btn-rectangle btn-wd" onClick={this._setLocalStorage.bind(null,event.eid,event.eventImage)}>자세히 보기</button>
                    </Link>
                  </td>
                </tr>
            ))}
          </tbody>
        </table>
        <div >
          <Link to="./manager_UploadEvent">
            <button className="btn btn-fill btn-rectangle btn-wd">행사 추가</button>
          </Link>
        </div>
      </div>
    </div>
    )
  }
}


export default ManagerEventTable;