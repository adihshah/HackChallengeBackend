import json
from db import db, Job, User
from flask import Flask, request

app = Flask(__name__)
db_filename = 'todo.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()
'''
Jason
/api/jobs/ GET
/api/job/<int:id>/ GET
/api/job/ POST
/api/job/<int:id>/ DELETE
/api/user/ POST
/api/user/<int:user_id>/ GET
/api/user/<int:user_id>/job/<int:job_id>/ POST (assign user u to job j)
'''
# Aditya
# DELETE /
# UPDATE ^
# CREATE NEW USER /api/users POST
# GET USER /api/user/i GET


# OAuth (Google)

# Later
# Connect to frontend
# Deployment

def serialize(iter):
    return [i.serialize() for i in iter]


def get_query_by_id(q, id):
    return q.query.filter_by(id=id).first()


@app.route('/api/jobs/')
def get_jobs():
    """ Returns all jobs. """
    jobs = Job.query.all()
    res = {'Success': True, 'Data': serialize(jobs)}
    return json.dumps(res), 200


@app.route('/api/job/', methods=['POST'])
def create_job():
    """ Creates a new job. """
    try:
        body = json.loads(request.data)
    except KeyError:
        return json.dumps({'Success': False, 'Error': 'No json provided!'}), 400

    job = Job(
        title=body.get('title'),
        description=body.get('description'),
        category=body.get('category'),
        starttime=body.get('starttime'),
        deadline=body.get('deadline'),
        startloc=body.get('startloc'),
        endloc=body.get('endloc'),
    )

    db.session.add(job)
    db.session.commit()
    return json.dumps({'Success': True, 'Data': job.serialize()}), 201


@app.route('/api/job/<int:id>/')
def get_job_by_id(id):
    """ Returns specific job with the given job id. """
    job = get_query_by_id(Job, id)
    if job is not None:
        return json.dumps({'Success': True, 'Data': job.serialize()}), 200
    return json.dumps({'Success': False, 'Error': 'Job not found!'}), 404


@app.route('/api/job/<int:id>/', methods=['DELETE'])
def delete_job(id):
    job = get_query_by_id(Job, id)
    if job is not None:
        db.session.delete(job)
        db.session.commit()
        return json.dumps({'Success': True, 'Data': job.serialize()}), 200
    return json.dumps({'Success': False, 'Error': 'Job not found'}), 404


# '''
# @app.route('/api/post/<int:post_id>/', methods=['POST'])
# def update_post(post_id):
#     post = Post.query.filter_by(id=post_id).first()

#     if post is not None:
#         post_body = json.loads(request.data)
#         post.text = post_body.get('text', post.text)
#         db.session.commit()
#         return json.dumps({'Success': True, 'Data': post.serialize()}), 200
#     return json.dumps({'Success': False, 'Error': 'Post not found'}), 404'''


# @app.route('/api/class/<int:class_id>/assignment/', methods=['POST'])
# def create_assignment(class_id):
#     clas = Class.query.filter_by(id=class_id).first()

#     if clas is not None:
#         clas_body = json.loads(request.data)
#         assignment = Assignment(
#             description=clas_body.get('description'),
#             due_date=clas_body.get('due_date'),
#             class_id=class_id
#         )
#         clas.assignments.append(assignment)
#         db.session.add(assignment)
#         db.session.commit()
#         return json.dumps({'Success': True, 'Data': assignment.serialize()}), 200
#     return json.dumps({'Success': False, 'Error': 'Post not found'}), 404


@app.route('/api/user/', methods=['POST'])
def create_user():
    """ Create a new user. """
    try:
        body = json.loads(request.data)
    except KeyError:
        return json.dumps({'success': False, 'error': 'No json provided!'}), 400

    user = User(
        name=body.get('name'),
        netid=body.get('netid'),
        phone_num=body.get('phone_num'),
        rating=body.get('rating'),
        jobs_completed=body.get('jobs_completed'),
        jobs_requested=body.get('jobs_requested'),
    )

    db.session.add(user)
    db.session.commit()
    return json.dumps({'success': True, 'data': user.serialize()}), 201


@app.route('/api/user/<int:user_id>/')
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is not None:
        return json.dumps({'Success': True, 'Data': user.serialize()}), 200
    return json.dumps({'Success': False, 'Error': 'User not found'}), 404


@app.route('/api/user/<int:user_id>/job/<int:job_id>/', methods=['POST'])
def add_user_to_job(user_id, job_id):
    """ Adds a user (user_id) to a specific job (job_id). """
    try:
        body = json.loads(request.data)
    except KeyError:
        return json.dumps({'success': False, 'error': 'No json Provided!'}), 400

    user_type = body.get('type')

    optional_job = get_query_by_id(Job, job_id)
    if optional_job is None:
        return json.dumps({'success': False, 'error': 'Job not found!'}), 404

    optional_user = get_query_by_id(User, user_id)
    if optional_user is None:
        return json.dumps({'success': False, 'error': 'User not found!'}), 404

    if user_type == "boss":
        optional_job.bosses.append(optional_user)
    else:
        optional_job.workers.append(optional_user)

    db.session.add(optional_job)
    db.session.commit()
    return json.dumps({'success': True, 'data': optional_job.serialize()}), 200


'''@app.route('/api/post/<int:post_id>/comment/', methods=['POST'])
def post_comment(post_id):
    post = Post.query.filter_by(id=post_id).first()

    if post is not None:
        post_body = json.loads(request.data)

        comment = Comment(

            text=(post_body.get('text')),
            username=post_body.get('username')
            score=0,
            post_id=post.id,

        )

        post.comments.append(comment)
        db.session.add(comment)
        db.session.commit()
        return json.dumps({'Success': True, 'Data': comment.serialize()}), 200
    return json.dumps({'Success': False, 'Error': 'Post not found'}), 404'''


'''@app.route('/api/post/<int:post_id>/comments/')
def get_comments(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is not None:
        comments = [comment.serialize() for comment in post.comments]
        return json.dumps({'Success': True, 'Data': comments}), 200
    return json.dumps({'Success': False, 'Error': 'Post not found'}), 404'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)