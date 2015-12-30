/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package {{package_name}}.activity;

import android.app.Activity;
import android.content.Context;

import {{package_name}}.R;
import {{package_name}}.mvp.presenters.{{presenter_name}};
import {{package_name}}.mvp.views.{{view_name}};

/**
 * Created by {{author}} on {{create_time}}.
 */
public class {{activity_name}} extends Activity implements {{view_name}} {

    public static final String TAG = "{{activity_name}}";

    private {{presenter_name}} mPresenter;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.your_activity_layout);
        setupData();
        setupViews(null);
    }

    private void setupData() {

    }

    @Override
    public void setupViews(View rootView) {

    }

    @Override
    public Context getContext() {
        return this;
    }

    @Override
    protected void onStart() {
        super.onStart();
        this.mPresenter.start();
    }

    @Override
    protected void onStop() {
        super.onStop();
        this.mPresenter.stop();
    }
}
