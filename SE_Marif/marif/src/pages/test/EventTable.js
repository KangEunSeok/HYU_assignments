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

  _setLocalStorage = (_eid) => {
    localStorage.setItem('eid',_eid)
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
                <th>상태 </th>
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
                    {moment(event.event_date).format('YYYY-MM-DD')}
                  </td>
                  <td>
                    {event.max_participant > event.current_participant ? "신청가능" : "신청불가"}
                  </td>
                  <td className="td-actions">
                    <Link to="/Event">
                      <button className="btn btn-fill btn-rectangle btn-wd" onClick={this._setLocalStorage.bind(null,event.eid)}>자세히 보기</button>
                    </Link>
                  </td>
                </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
    )
  }
}


export default EventTable;