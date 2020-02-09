import React, { Component } from 'react';
import NotificationSystem from 'react-notification-system';

const axios = require('axios');

class ProfileValid extends Component {
  constructor(props) {
    super(props);
    this.handlePassword = this.handlePassword.bind(this);
    this.state = {
      passWord: '',
      valid: false,
    };
  }
  
  handlePassword(e){
    this.setState({passWord:e.target.value})
  }

  _checkPassword = async () => {
    const userInfo = await this.checkPasswordApi()
    if (userInfo===null){

    }else{
      this.setState({userInfo: userInfo})
      this.setState({valid : true})
    }
    console.log(this.state.userInfo)
  }
  checkPasswordApi = () => {
    let data= new FormData();
    data.append('id',localStorage.getItem('userId'));
    data.append('password', this.state.passWord);
    return axios.post('http://54.180.25.155:8020/users/login', data)
    .then(response => response.data)
    .catch(err => console.log(err))
  }

  render() {
    return (
       <div className="content">
        <div className="container-fluid">
          <div className="card">
            <div className="header">
              <h4>프로필 변경</h4>
            </div>
            <div className="content">
              <div className="places-buttons">
                <div className="row">
                  <div className="col-md-6 col-md-offset-3 text-center">
                    <h5>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                     비밀 번호를 입력하세요
                      <p className="category"></p>
                      <div className="form-group">
                      <label className="col-sm-3 control-label"></label>
                      <div className="col-sm-5">
                        <input className="" value={this.state.passWord} onChange={this.handlePassword}/> 
                      </div>
                      <div className='col-sm-18'>
                          <button className="btn btn-rectangle btn-xs btn-fill" onClick={this._checkPassword}>확인</button>
                      </div>
                      </div>
                    </h5>
                  </div>
                </div>
                
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }
}
export default ProfileValid;