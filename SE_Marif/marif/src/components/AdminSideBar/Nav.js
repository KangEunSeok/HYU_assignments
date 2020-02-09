import React, { Component } from 'react';
import { Link, withRouter } from 'react-router-dom';


class Nav extends Component {

  state = {};

  render() {
    let { location } = this.props;
    return (
      <ul className="nav">
        <li className={location.pathname === '/manager_ManageEvent' ? 'active' : null}>
          <Link to="/manager_ManageEvent">
            <i className="pe-7s-graph"></i>
            <p>관리자 행사목록</p>
          </Link>
        </li>
      </ul>
    );
  }

  isPathActive(path) {
    return this.props.location.pathname.startsWith(path);
  }
}

export default withRouter(Nav);