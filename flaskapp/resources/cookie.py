from api.models import Cookie
from flask_restful import Resource


class CookieListAPI(Resource):
    '''
    This handles listing collections.
    GET /cookies/api/v1.0/cookies for reading all cookies
    POST /cookies/api/v1.0/cookies for creates
    '''

    def get(self):
        # test = db.session.query.filter_by(cookie_name='test').all()
        test = Cookie.query.filter_by(cookie_name='test').first_or_404()
        print(test.cookie_id)
        return test

    def post(self):
        pass


class CookieAPI(Resource):
    '''
    Handles single resource operations
    GET /cookies/api/v1.0/cookies/<int:id> for reads
    PUT /cookies/api/v1.0/cookies/<int:id> for updates
    DELETE /cookies/api/v1.0/cookies/<int:id> for deletes
    '''

    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass
